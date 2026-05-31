# Decision Report

- generated_at: 2026-05-31T02:10:42.810508+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5164**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5164, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.41%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.41% | **-0.41%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_FIB1618 | 4/20 | 20.0% | +2.78% | **+0.56%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.67% | **+0.50%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.70% | **+1.61%** |
| ASK_LONG | 20/20 | 100.0% | +1.34% | **+1.34%** |
| MARKET_LONG | 20/20 | 100.0% | +1.19% | **+1.19%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.38% | **+0.97%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.17% | **+0.94%** |

## 2. $100 Live Portfolio

- 残高: **$97.61** / 初期 $100.00 (-2.39%)
- 確定トレード: 79件 (TP 23 / SL 53 / EXP 3)
- 最新: ID/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$122.91** / 初期 $100.00 (+22.91%)
- 確定: 801件 (Win 184 / Loss 243 / Flat 374) / skip 924件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +6.32%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TA/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $122.91

## 4. Latest Market Context

- 更新: 2026-05-31T02:10:40.341352+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=74072.7
- Funnel: target 773 → liquid 120 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +58.20% | $8,599,434.82 |
| TA/USDT:USDT | +35.01% | $2,166,068.88 |
| STG/USDT:USDT | +12.47% | $3,729,112.93 |
| NFP/USDT:USDT | +8.69% | $4,325,938.72 |
| ONDO/USDT:USDT | +8.55% | $36,340,739.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TA/USDT:USDT | below_1h_threshold | +4.52% | +4.45% |
| PORTAL/USDT:USDT | below_1h_threshold | +4.31% | +4.24% |
| BIANRENSHENG/USDT:USDT | below_1h_threshold | +1.45% | +1.38% |
| BASED/USDT:USDT | below_1h_threshold | +0.84% | +0.77% |
| NEX/USDT:USDT | below_1h_threshold | +0.75% | +0.68% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
