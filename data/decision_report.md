# Decision Report

- generated_at: 2026-06-10T10:37:13.882734+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6209**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6209, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.85% | **+0.55%** |
| ASK | 20/20 | 100.0% | +0.41% | **+0.41%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.14% | **+0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| ASK_LONG | 20/20 | 100.0% | +0.96% | **+0.96%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +2.08% | **+0.83%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.10% | **+0.38%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +0.40% | **+0.26%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$152.02** / 初期 $100.00 (+52.02%)
- 確定: 1225件 (Win 306 / Loss 380 / Flat 539) / skip 1545件
- 成長率目線: 平均log +0.000342 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $152.02

## 4. Latest Market Context

- 更新: 2026-06-10T10:37:10.936611+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=61329.6
- Funnel: target 785 → liquid 150 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STG/USDT:USDT | +47.36% | $11,718,609.26 |
| BLEND/USDT:USDT | +45.95% | $1,327,871.07 |
| ESPORTS/USDT:USDT | +36.82% | $27,023,575.11 |
| KAT/USDT:USDT | +31.31% | $1,105,153.75 |
| BTW/USDT:USDT | +20.25% | $31,147,129.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLEND/USDT:USDT | below_1h_threshold | +4.27% | +4.23% |
| KAT/USDT:USDT | below_1h_threshold | +3.39% | +3.34% |
| UB/USDT:USDT | below_1h_threshold | +2.24% | +2.19% |
| HOME/USDT:USDT | below_1h_threshold | +1.74% | +1.70% |
| IO/USDT:USDT | below_1h_threshold | +1.39% | +1.35% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
