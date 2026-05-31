# Decision Report

- generated_at: 2026-05-31T05:11:17.764572+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5173**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5173, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.23% | **-0.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_FIB1618 | 4/20 | 20.0% | +2.98% | **+0.60%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.67% | **+0.50%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.97% | **+0.92%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.19% | **+0.65%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +3.22% | **+0.48%** |

## 2. $100 Live Portfolio

- 残高: **$97.61** / 初期 $100.00 (-2.39%)
- 確定トレード: 79件 (TP 23 / SL 53 / EXP 3)
- 最新: ID/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$122.91** / 初期 $100.00 (+22.91%)
- 確定: 808件 (Win 184 / Loss 243 / Flat 381) / skip 926件
- 成長率目線: 平均log +0.000255 / 幾何平均 +0.026% per trade / maxDD +6.32%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $122.91

## 4. Latest Market Context

- 更新: 2026-05-31T05:11:15.187820+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=74163.5
- Funnel: target 773 → liquid 123 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +31.69% | $10,465,762.63 |
| PUNDIX/USDT:USDT | +29.56% | $1,168,981.30 |
| TA/USDT:USDT | +20.54% | $2,346,905.51 |
| MYX/USDT:USDT | +14.49% | $2,223,989.98 |
| STG/USDT:USDT | +9.86% | $4,162,971.49 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MYX/USDT:USDT | below_1h_threshold | +4.43% | +4.41% |
| H/USDT:USDT | below_1h_threshold | +3.12% | +3.11% |
| IO/USDT:USDT | below_1h_threshold | +1.01% | +1.00% |
| PUNDIX/USDT:USDT | below_1h_threshold | +0.93% | +0.91% |
| UP/USDT:USDT | below_1h_threshold | +0.84% | +0.82% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
