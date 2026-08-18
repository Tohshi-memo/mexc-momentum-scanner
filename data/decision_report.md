# Decision Report

- generated_at: 2026-08-18T12:06:23.396046+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11901**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.93% / filled 20/20。**
- 全期間 MARKET基準: n=11901, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.93%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.93% | **+1.93%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.93% | **+1.93%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.43% | **+1.21%** |
| LIMIT_4PCT | 10/20 | 50.0% | +1.60% | **+0.80%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.22% | **+0.36%** |
| LIMIT_ATR | 8/20 | 40.0% | +0.87% | **+0.35%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +4.55% | **+1.36%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +2.67% | **+1.20%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.80% | **+0.90%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.83% | **+0.54%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.53% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定トレード: 187件 (TP 72 / SL 110 / EXP 5)
- 最新: HEMI/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.41
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$617.35** / 初期 $100.00 (+517.35%)
- 確定: 4201件 (Win 1295 / Loss 1372 / Flat 1534) / skip 4261件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIULAI/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account -0.13% 残高後 $617.35

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.25** / 初期 $100.00 (+55.25%)
- 確定: 1819件 (Win 502 / Loss 427 / Flat 890) / skip 3493件
- 成長率目線: 平均log +0.000242 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0044 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $155.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.85** / 初期 $100.00 (+18.85%)
- 確定: 1712件 (Win 512 / Loss 649 / Flat 551) / pending 6件 / skip 1657件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000428 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: H/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $118.85

## 6. Latest Market Context

- 更新: 2026-08-18T12:06:14.866389+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=64320.0
- Funnel: target 993 → liquid 177 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PRL/USDT:USDT | +19.74% | $3,593,285.80 |
| GPS/USDT:USDT | +16.17% | $30,757,629.15 |
| VVV/USDT:USDT | +15.81% | $7,317,517.07 |
| RED/USDT:USDT | +15.26% | $3,434,929.78 |
| OPN/USDT:USDT | +13.99% | $2,387,317.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +1.15% | +1.16% |
| HEMI/USDT:USDT | below_1h_threshold | +0.86% | +0.87% |
| GUN/USDT:USDT | below_1h_threshold | +0.84% | +0.85% |
| ACE/USDT:USDT | below_1h_threshold | +0.80% | +0.81% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +0.63% | +0.64% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
