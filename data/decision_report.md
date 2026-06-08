# Decision Report

- generated_at: 2026-06-08T14:01:13.857750+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6079**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6079, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.93%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.93% | **-0.93%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.29% | **-0.20%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.81% | **-0.28%** |
| LIMIT_BB3S | 4/16 | 25.0% | -2.51% | **-0.63%** |
| LIMIT_3PCT | 14/20 | 70.0% | -1.19% | **-0.83%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.53% | **+1.53%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.43% | **+1.07%** |
| ASK_LONG | 20/20 | 100.0% | +0.96% | **+0.96%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.39% | **+0.70%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +1.60% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$97.59** / 初期 $100.00 (-2.41%)
- 確定トレード: 9件 (TP 1 / SL 7 / EXP 1)
- 最新: SKYAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.59
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.21** / 初期 $100.00 (+51.21%)
- 確定: 1144件 (Win 280 / Loss 350 / Flat 514) / skip 1496件
- 成長率目線: 平均log +0.000361 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $151.21

## 4. Latest Market Context

- 更新: 2026-06-08T14:01:10.876986+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=63710.0
- Funnel: target 777 → liquid 149 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALLO/USDT:USDT | +55.96% | $77,165,218.56 |
| BEAT/USDT:USDT | +51.41% | $147,761,905.97 |
| VELVET/USDT:USDT | +51.08% | $8,973,588.09 |
| PIPPIN/USDT:USDT | +37.76% | $15,724,915.62 |
| MOVE/USDT:USDT | +24.14% | $1,224,496.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STG/USDT:USDT | below_1h_threshold | +0.57% | +0.60% |
| FHE/USDT:USDT | below_1h_threshold | +0.56% | +0.58% |
| BEAT/USDT:USDT | below_1h_threshold | +0.49% | +0.51% |
| MOVE/USDT:USDT | below_1h_threshold | +0.41% | +0.43% |
| EWY/USDT:USDT | below_1h_threshold | +0.35% | +0.37% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
