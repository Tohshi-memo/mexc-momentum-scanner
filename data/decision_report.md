# Decision Report

- generated_at: 2026-06-06T20:53:16.571311+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5903**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5903, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +2.06% | **+0.41%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.50% | **+0.28%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +5.83% | **+4.16%** |
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.82% | **+1.37%** |
| ASK_LONG | 20/20 | 100.0% | +1.36% | **+1.36%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +1.69% | **+0.93%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 2件 (TP 0 / SL 2 / EXP 0)
- 最新: PORTAL/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$136.40** / 初期 $100.00 (+36.40%)
- 確定: 1036件 (Win 248 / Loss 318 / Flat 470) / skip 1428件
- 成長率目線: 平均log +0.000300 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $136.40

## 4. Latest Market Context

- 更新: 2026-06-06T20:53:12.050743+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=60677.5
- Funnel: target 771 → liquid 129 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +52.52% | $55,449,670.43 |
| BTW/USDT:USDT | +34.49% | $15,400,098.00 |
| SKYAI/USDT:USDT | +34.28% | $19,868,222.20 |
| FIDA/USDT:USDT | +29.92% | $2,136,487.75 |
| BLUAI/USDT:USDT | +8.78% | $7,229,263.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALLO/USDT:USDT | below_1h_threshold | +4.52% | +4.33% |
| B/USDT:USDT | below_1h_threshold | +3.53% | +3.34% |
| FIDA/USDT:USDT | below_1h_threshold | +2.45% | +2.26% |
| UB/USDT:USDT | below_1h_threshold | +2.23% | +2.04% |
| SLX/USDT:USDT | below_1h_threshold | +2.08% | +1.89% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
