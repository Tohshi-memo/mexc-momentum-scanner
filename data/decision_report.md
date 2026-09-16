# Decision Report

- generated_at: 2026-09-16T03:41:47.703476+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14628**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.46% / filled 20/20。**
- 全期間 MARKET基準: n=14628, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+3.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.46% | **+3.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.46% | **+3.46%** |
| LIMIT_1PCT | 17/20 | 85.0% | +3.68% | **+3.13%** |
| LIMIT_2PCT | 13/20 | 65.0% | +2.93% | **+1.91%** |
| LIMIT_ATR | 11/20 | 55.0% | +3.33% | **+1.83%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +3.59% | **+0.90%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +0.73% | **+0.40%** |
| LIMIT_7PCT_LONG | 13/20 | 65.0% | +0.30% | **+0.19%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| LIMIT_6PCT_LONG | 13/20 | 65.0% | -0.52% | **-0.34%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | -1.19% | **-0.36%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,044.12** / 初期 $100.00 (+944.12%)
- 確定: 5517件 (Win 1645 / Loss 1786 / Flat 2086) / skip 5672件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIN/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $1,044.12

## 4. Robust Adaptive DryRun ($100)

- 残高: **$230.42** / 初期 $100.00 (+130.42%)
- 確定: 3054件 (Win 839 / Loss 719 / Flat 1496) / skip 4985件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0238 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $230.42

## 5. Causal Adaptive DryRun ($100)

- 残高: **$125.15** / 初期 $100.00 (+25.15%)
- 確定: 2919件 (Win 868 / Loss 1138 / Flat 913) / pending 3件 / skip 3177件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000374 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LSK/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $125.15

## 6. Latest Market Context

- 更新: 2026-09-16T03:41:25.182596+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=75801.6
- Funnel: target 1061 → liquid 154 → pre 50 → checked 50 → surge 4 → strict 3
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +28.06% | $2,135,795.00 |
| LSK/USDT:USDT | +27.96% | $16,265,319.46 |
| ON/USDT:USDT | +14.63% | $3,113,901.67 |
| LONGXIA/USDT:USDT | +13.73% | $1,818,061.84 |
| USELESS/USDT:USDT | +9.61% | $5,061,671.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MARSCOIN/USDT:USDT | below_1h_threshold | +4.88% | +4.95% |
| BTW/USDT:USDT | below_1h_threshold | +3.22% | +3.29% |
| LONGXIA/USDT:USDT | below_1h_threshold | +3.20% | +3.27% |
| KORU/USDT:USDT | below_1h_threshold | +2.71% | +2.78% |
| USELESS/USDT:USDT | below_1h_threshold | +1.75% | +1.81% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
