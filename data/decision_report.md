# Decision Report

- generated_at: 2026-06-02T22:28:39.464764+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5496**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5496, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.48% | **-1.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +2.82% | **+0.99%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.52% | **+0.63%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.67% | **+0.47%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.63% | **+0.39%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.69% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +3.65% | **+2.43%** |
| MARKET_LONG | 20/20 | 100.0% | +1.78% | **+1.78%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.18% | **+1.74%** |
| ASK_LONG | 20/20 | 100.0% | +1.73% | **+1.73%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.34% | **+1.52%** |

## 2. $100 Live Portfolio

- 残高: **$96.61** / 初期 $100.00 (-3.39%)
- 確定トレード: 90件 (TP 26 / SL 61 / EXP 3)
- 最新: VVV/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.39** / 初期 $100.00 (+30.39%)
- 確定: 976件 (Win 229 / Loss 300 / Flat 447) / skip 1081件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $130.39

## 4. Latest Market Context

- 更新: 2026-06-02T22:28:36.276010+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=67381.1
- Funnel: target 769 → liquid 152 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +36.70% | $6,749,793.84 |
| PORTAL/USDT:USDT | +34.28% | $12,743,263.31 |
| BBSTOCK/USDT:USDT | +18.33% | $1,708,830.88 |
| LIT/USDT:USDT | +16.62% | $6,531,092.55 |
| MRVLSTOCK/USDT:USDT | +14.92% | $14,593,051.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +4.81% | +5.03% |
| BBSTOCK/USDT:USDT | below_1h_threshold | +1.57% | +1.79% |
| CHIP/USDT:USDT | below_1h_threshold | +1.20% | +1.42% |
| LIT/USDT:USDT | below_1h_threshold | +1.15% | +1.38% |
| W/USDT:USDT | below_1h_threshold | +1.04% | +1.26% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
