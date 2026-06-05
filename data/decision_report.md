# Decision Report

- generated_at: 2026-06-05T00:12:11.826169+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5682**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5682, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.08% | **-0.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.54% | **+0.38%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.32% | **+0.32%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.90% | **+0.95%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.62% | **+0.65%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +1.23% | **+0.49%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.75% | **+0.41%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +1.60% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$98.05** / 初期 $100.00 (-1.95%)
- 確定トレード: 99件 (TP 30 / SL 66 / EXP 3)
- 最新: MONAD/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.05
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1008件 (Win 239 / Loss 312 / Flat 457) / skip 1235件
- 成長率目線: 平均log +0.000269 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: OPN/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-05T00:12:09.191041+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=63731.6
- Funnel: target 771 → liquid 166 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 97.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +95.21% | $9,638,189.89 |
| HOME/USDT:USDT | +29.36% | $7,031,273.74 |
| OPN/USDT:USDT | +19.91% | $37,379,590.50 |
| AAOISTOCK/USDT:USDT | +9.71% | $1,272,566.65 |
| XMR/USDT:USDT | +8.94% | $10,852,484.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HEI/USDT:USDT | below_1h_threshold | +3.09% | +3.28% |
| OPN/USDT:USDT | below_1h_threshold | +2.15% | +2.34% |
| BEAT/USDT:USDT | below_1h_threshold | +1.35% | +1.54% |
| LUNC/USDT:USDT | below_1h_threshold | +1.32% | +1.51% |
| HOME/USDT:USDT | below_1h_threshold | +1.18% | +1.37% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
