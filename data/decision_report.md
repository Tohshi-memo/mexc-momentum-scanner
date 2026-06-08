# Decision Report

- generated_at: 2026-06-08T07:01:49.991194+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6042**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6042, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.20% | **-0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.30% | **+0.13%** |
| ASK | 20/20 | 100.0% | +0.07% | **+0.07%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +2.07% | **+1.24%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.48% | **+1.04%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.68% | **+1.01%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.64% | **+0.90%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.33% | **+0.87%** |

## 2. $100 Live Portfolio

- 残高: **$97.59** / 初期 $100.00 (-2.41%)
- 確定トレード: 9件 (TP 1 / SL 7 / EXP 1)
- 最新: SKYAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.59
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.21** / 初期 $100.00 (+51.21%)
- 確定: 1144件 (Win 280 / Loss 350 / Flat 514) / skip 1459件
- 成長率目線: 平均log +0.000361 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $151.21

## 4. Latest Market Context

- 更新: 2026-06-08T07:01:46.600659+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=62918.8
- Funnel: target 773 → liquid 141 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BEAT/USDT:USDT | +44.33% | $106,008,203.20 |
| ALLO/USDT:USDT | +32.81% | $36,232,538.02 |
| ESPORTS/USDT:USDT | +28.31% | $7,262,598.16 |
| PIPPIN/USDT:USDT | +27.49% | $9,151,754.02 |
| BANK/USDT:USDT | +17.39% | $5,127,932.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +2.45% | +2.51% |
| BEAT/USDT:USDT | below_1h_threshold | +0.84% | +0.90% |
| PIPPIN/USDT:USDT | below_1h_threshold | +0.82% | +0.87% |
| ZEC/USDT:USDT | below_1h_threshold | +0.46% | +0.51% |
| RAVE/USDT:USDT | below_1h_threshold | +0.32% | +0.38% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
