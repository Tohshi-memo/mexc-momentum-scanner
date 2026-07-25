# Decision Report

- generated_at: 2026-07-25T04:01:08.744440+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9480**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.54% / filled 20/20。**
- 全期間 MARKET基準: n=9480, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.54%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.54% | **+0.54%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.54% | **+0.54%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.96% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.97% | **+1.08%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.71% | **+0.61%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.86% | **+0.60%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.57% | **+0.55%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +2.81% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$103.79** / 初期 $100.00 (+3.79%)
- 確定トレード: 139件 (TP 46 / SL 88 / EXP 5)
- 最新: SYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.79
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$423.36** / 初期 $100.00 (+323.36%)
- 確定: 3326件 (Win 1048 / Loss 1077 / Flat 1201) / skip 2715件
- 成長率目線: 平均log +0.000434 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DEXE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $423.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.36** / 初期 $100.00 (+30.36%)
- 確定: 1165件 (Win 312 / Loss 254 / Flat 599) / skip 1726件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0794 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $130.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$104.51** / 初期 $100.00 (+4.51%)
- 確定: 531件 (Win 177 / Loss 208 / Flat 146) / pending 3件 / skip 416件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000262 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ZAMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $104.51

## 6. Latest Market Context

- 更新: 2026-07-25T04:01:02.042553+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=64061.3
- Funnel: target 898 → liquid 162 → pre 50 → checked 49 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=1

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DEXE/USDT:USDT | +62.66% | $50,547,273.64 |
| SLX/USDT:USDT | +13.89% | $2,482,533.27 |
| ACE/USDT:USDT | +12.74% | $9,697,448.16 |
| ZAMA/USDT:USDT | +12.26% | $3,073,468.77 |
| SAGA/USDT:USDT | +9.90% | $1,269,059.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +1.22% | +1.21% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.00% | +0.98% |
| PONS/USDT:USDT | below_1h_threshold | +0.55% | +0.54% |
| B2/USDT:USDT | below_1h_threshold | +0.54% | +0.53% |
| ZAMA/USDT:USDT | below_1h_threshold | +0.50% | +0.48% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
