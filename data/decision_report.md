# Decision Report

- generated_at: 2026-06-03T09:20:20.810584+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5538**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5538, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.24% | **-1.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 18/20 | 90.0% | +1.28% | **+1.15%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.96% | **+0.69%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.48% | **+0.52%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.57% | **+0.40%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.44% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.72% | **+0.86%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.61% | **+0.80%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.10% | **+0.77%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.11% | **+0.67%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.44% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$96.61** / 初期 $100.00 (-3.39%)
- 確定トレード: 90件 (TP 26 / SL 61 / EXP 3)
- 最新: VVV/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.88** / 初期 $100.00 (+30.88%)
- 確定: 992件 (Win 235 / Loss 306 / Flat 451) / skip 1107件
- 成長率目線: 平均log +0.000271 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLO/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $130.88

## 4. Latest Market Context

- 更新: 2026-06-03T09:20:18.332110+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.25% price=66819.9
- Funnel: target 771 → liquid 153 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLO/USDT:USDT | +42.15% | $3,860,956.20 |
| PORTAL/USDT:USDT | +31.27% | $14,585,803.92 |
| GENIUS/USDT:USDT | +30.10% | $1,944,680.82 |
| APR/USDT:USDT | +23.57% | $1,385,358.10 |
| ENA/USDT:USDT | +23.34% | $50,696,203.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| INTCSTOCK/USDT:USDT | below_1h_threshold | +3.03% | +3.28% |
| US/USDT:USDT | below_1h_threshold | +2.63% | +2.88% |
| AIA/USDT:USDT | below_1h_threshold | +2.26% | +2.51% |
| GUA/USDT:USDT | below_1h_threshold | +2.13% | +2.38% |
| ZORA/USDT:USDT | below_1h_threshold | +1.57% | +1.82% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
