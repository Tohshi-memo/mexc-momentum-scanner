# Decision Report

- generated_at: 2026-10-19T04:36:43.891177+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16980**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16980, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-2.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.10% | **-2.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 18/20 | 90.0% | +0.81% | **+0.72%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.75% | **+0.60%** |
| LIMIT_FIB1272 | 12/20 | 60.0% | +0.93% | **+0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +4.30% | **+2.36%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +4.03% | **+2.22%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +4.00% | **+1.80%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +4.57% | **+1.60%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.58% | **+1.43%** |

## 2. $100 Live Portfolio

- 残高: **$121.60** / 初期 $100.00 (+21.60%)
- 確定トレード: 245件 (TP 91 / SL 147 / EXP 7)
- 最新: ICNT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.60
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,287.67** / 初期 $100.00 (+1187.67%)
- 確定: 6425件 (Win 1868 / Loss 2052 / Flat 2505) / skip 7116件
- 成長率目線: 平均log +0.000398 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZEREBRO/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $1,287.67

## 4. Robust Adaptive DryRun ($100)

- 残高: **$276.84** / 初期 $100.00 (+176.84%)
- 確定: 3745件 (Win 1034 / Loss 881 / Flat 1830) / skip 6646件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0792 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ZEREBRO/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $276.84

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5145件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000166 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-19T04:36:21.653802+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=82600.5
- Funnel: target 1084 → liquid 145 → pre 50 → checked 50 → surge 4 → strict 3
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZEREBRO/USDT:USDT | +32.20% | $1,397,499.93 |
| Q/USDT:USDT | +29.97% | $10,347,112.86 |
| KORU/USDT:USDT | +16.65% | $47,563,846.02 |
| AGT/USDT:USDT | +12.54% | $7,452,327.73 |
| SNXX/USDT:USDT | +12.23% | $12,061,787.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BR/USDT:USDT | below_1h_threshold | +2.64% | +2.52% |
| SAND/USDT:USDT | below_1h_threshold | +1.83% | +1.70% |
| KORU/USDT:USDT | below_1h_threshold | +1.78% | +1.66% |
| ZRO/USDT:USDT | below_1h_threshold | +1.29% | +1.16% |
| CRV/USDT:USDT | below_1h_threshold | +1.25% | +1.12% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
