# Decision Report

- generated_at: 2026-05-31T03:29:09.825215+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5168**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5168, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.57%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.57% | **-0.57%** |

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
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.31% | **+1.25%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.69% | **+1.18%** |
| ASK_LONG | 20/20 | 100.0% | +1.08% | **+1.08%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.28% | **+1.02%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +2.00% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$97.61** / 初期 $100.00 (-2.39%)
- 確定トレード: 79件 (TP 23 / SL 53 / EXP 3)
- 最新: ID/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$122.91** / 初期 $100.00 (+22.91%)
- 確定: 804件 (Win 184 / Loss 243 / Flat 377) / skip 925件
- 成長率目線: 平均log +0.000257 / 幾何平均 +0.026% per trade / maxDD +6.32%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STG/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $122.91

## 4. Latest Market Context

- 更新: 2026-05-31T03:29:08.098079+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=74153.4
- Funnel: target 773 → liquid 124 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +44.47% | $9,632,219.90 |
| TA/USDT:USDT | +20.13% | $2,295,810.92 |
| STG/USDT:USDT | +17.58% | $3,871,215.17 |
| GENIUS/USDT:USDT | +10.88% | $1,037,892.02 |
| NFP/USDT:USDT | +10.46% | $4,427,615.91 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BASED/USDT:USDT | below_1h_threshold | +3.05% | +2.92% |
| FLOKI/USDT:USDT | below_1h_threshold | +1.99% | +1.87% |
| ENA/USDT:USDT | below_1h_threshold | +1.03% | +0.91% |
| MNT/USDT:USDT | below_1h_threshold | +1.01% | +0.88% |
| ID/USDT:USDT | below_1h_threshold | +0.98% | +0.86% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
