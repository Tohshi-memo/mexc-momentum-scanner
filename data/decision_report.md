# Decision Report

- generated_at: 2026-06-09T16:49:40.973730+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6151**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6151, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +1.02% | **+0.82%** |
| ASK | 20/20 | 100.0% | +0.23% | **+0.23%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.06% | **+0.02%** |
| LIMIT_1PCT | 18/20 | 90.0% | -0.09% | **-0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.54% | **+1.00%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.23% | **+0.80%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +1.07% | **+0.64%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.12% | **+0.56%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +4.93% | **+0.49%** |

## 2. $100 Live Portfolio

- 残高: **$96.14** / 初期 $100.00 (-3.86%)
- 確定トレード: 12件 (TP 1 / SL 10 / EXP 1)
- 最新: SIREN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.14
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$148.01** / 初期 $100.00 (+48.01%)
- 確定: 1188件 (Win 297 / Loss 374 / Flat 517) / skip 1524件
- 成長率目線: 平均log +0.000330 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EPIC/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $148.01

## 4. Latest Market Context

- 更新: 2026-06-09T16:49:37.803407+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.25% price=61254.9
- Funnel: target 778 → liquid 156 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SIREN/USDT:USDT | +6.24% | $10,242,134.84 |
| ESPORTS/USDT:USDT | +3.63% | $25,016,977.30 |
| CHZ/USDT:USDT | +3.20% | $10,951,324.12 |
| PLAY/USDT:USDT | +2.64% | $2,878,721.67 |
| POL/USDT:USDT | +1.85% | $1,372,400.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +3.82% | +3.57% |
| CHZ/USDT:USDT | below_1h_threshold | +3.13% | +2.89% |
| HOME/USDT:USDT | below_1h_threshold | +2.61% | +2.37% |
| PLAY/USDT:USDT | below_1h_threshold | +2.09% | +1.84% |
| POL/USDT:USDT | below_1h_threshold | +1.86% | +1.61% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
