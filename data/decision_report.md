# Decision Report

- generated_at: 2026-08-14T14:31:30.389544+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11561**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.46% / filled 20/20。**
- 全期間 MARKET基準: n=11561, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.46% | **+1.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.46% | **+1.46%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.51% | **+1.28%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.46% | **+1.02%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.13% | **+1.02%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.41% | **+0.85%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.33% | **+0.82%** |
| LIMIT_9PCT_LONG | 8/20 | 40.0% | +1.32% | **+0.53%** |
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +0.62% | **+0.50%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.80% | **+0.48%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$626.17** / 初期 $100.00 (+526.17%)
- 確定: 4029件 (Win 1264 / Loss 1325 / Flat 1440) / skip 4093件
- 成長率目線: 平均log +0.000455 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACE/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $626.17

## 4. Robust Adaptive DryRun ($100)

- 残高: **$149.41** / 初期 $100.00 (+49.41%)
- 確定: 1651件 (Win 471 / Loss 398 / Flat 782) / skip 3321件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0180 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $149.41

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.68** / 初期 $100.00 (+17.68%)
- 確定: 1521件 (Win 461 / Loss 579 / Flat 481) / pending 6件 / skip 1508件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000262 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ACE/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $117.68

## 6. Latest Market Context

- 更新: 2026-08-14T14:31:20.971060+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=62638.2
- Funnel: target 985 → liquid 178 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.8 >= 65=1, 4h RSI 91.8 >= 65=1, 4h RSI 82.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACE/USDT:USDT | +141.73% | $38,892,219.06 |
| AKE/USDT:USDT | +65.80% | $69,000,764.49 |
| CAP/USDT:USDT | +39.31% | $6,002,328.93 |
| CROSS/USDT:USDT | +36.05% | $1,891,962.98 |
| VELVET/USDT:USDT | +26.43% | $39,071,003.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| APR/USDT:USDT | below_1h_threshold | +4.93% | +4.92% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +3.55% | +3.55% |
| TESLA/USDT:USDT | below_1h_threshold | +2.55% | +2.55% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +2.29% | +2.29% |
| USELESS/USDT:USDT | below_1h_threshold | +1.70% | +1.70% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
