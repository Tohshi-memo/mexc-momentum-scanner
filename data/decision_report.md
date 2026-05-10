# Decision Report

- generated_at: 2026-05-10T05:02:40.574470+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3941**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3941, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.32% | **-0.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.44% | **+0.36%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |
| LIMIT_BB3S | 2/17 | 11.8% | +2.00% | **+0.24%** |
| LIMIT_8PCT | 3/20 | 15.0% | +1.14% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.67% | **+1.59%** |
| MARKET_LONG | 20/20 | 100.0% | +1.22% | **+1.22%** |
| ASK_LONG | 20/20 | 100.0% | +1.14% | **+1.14%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +3.33% | **+1.00%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +1.50% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.73** / 初期 $100.00 (+7.73%)
- 確定: 197件 (Win 48 / Loss 66 / Flat 83) / skip 305件
- 成長率目線: 平均log +0.000378 / 幾何平均 +0.038% per trade / maxDD +4.09%
- 次の候補: `LIMIT_5PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAYER/USDT:USDT `LIMIT_5PCT_LONG` EXPIRED account +0.00% 残高後 $107.73

## 4. Latest Market Context

- 更新: 2026-05-10T05:02:37.436718+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=80680.0
- Funnel: target 769 → liquid 162 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAYER/USDT:USDT | +30.91% | $1,420,221.07 |
| SATO/USDT:USDT | +17.03% | $6,234,947.13 |
| INX/USDT:USDT | +15.21% | $15,041,309.96 |
| JASMY/USDT:USDT | +13.90% | $20,740,695.28 |
| AIGENSYN/USDT:USDT | +10.70% | $1,176,867.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAYER/USDT:USDT | below_1h_threshold | +4.62% | +4.67% |
| SATO/USDT:USDT | below_1h_threshold | +1.63% | +1.67% |
| VINE/USDT:USDT | below_1h_threshold | +1.25% | +1.30% |
| MITO/USDT:USDT | below_1h_threshold | +0.91% | +0.96% |
| BEAT/USDT:USDT | below_1h_threshold | +0.64% | +0.68% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
