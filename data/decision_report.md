# Decision Report

- generated_at: 2026-05-09T15:07:27.369514+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3890**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3890, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.42%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.42% | **-0.42%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/13 | 38.5% | +2.03% | **+0.78%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.44% | **+0.36%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.48% | **+0.34%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |
| ASK | 20/20 | 100.0% | +0.15% | **+0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.25% | **+1.13%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.14% | **+0.63%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.82% | **+0.45%** |
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +0.46% | **+0.33%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +0.24% | **+0.10%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.27** / 初期 $100.00 (+8.27%)
- 確定: 195件 (Win 48 / Loss 65 / Flat 82) / skip 256件
- 成長率目線: 平均log +0.000407 / 幾何平均 +0.041% per trade / maxDD +3.61%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account -0.13% 残高後 $108.27

## 4. Latest Market Context

- 更新: 2026-05-09T15:07:24.536795+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=80253.8
- Funnel: target 769 → liquid 175 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SAHARA/USDT:USDT | +32.94% | $4,608,244.54 |
| ZEREBRO/USDT:USDT | +31.56% | $3,521,622.20 |
| INX/USDT:USDT | +29.45% | $1,020,761.88 |
| DYM/USDT:USDT | +24.12% | $6,657,773.68 |
| BILL/USDT:USDT | +21.62% | $19,955,522.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BIO/USDT:USDT | below_1h_threshold | +1.22% | +1.27% |
| SAHARA/USDT:USDT | below_1h_threshold | +1.22% | +1.27% |
| PLAY/USDT:USDT | below_1h_threshold | +0.79% | +0.83% |
| OP/USDT:USDT | below_1h_threshold | +0.48% | +0.53% |
| DRAM/USDT:USDT | below_1h_threshold | +0.41% | +0.46% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
