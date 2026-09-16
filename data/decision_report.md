# Decision Report

- generated_at: 2026-09-16T04:26:25.712735+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14633**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.06% / filled 20/20。**
- 全期間 MARKET基準: n=14633, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.06% | **+1.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 14/20 | 70.0% | +1.60% | **+1.12%** |
| MARKET | 20/20 | 100.0% | +1.06% | **+1.06%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.98% | **+0.83%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.47% | **+0.62%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.68% | **+0.61%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.58% | **+0.26%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.30% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,044.12** / 初期 $100.00 (+944.12%)
- 確定: 5517件 (Win 1645 / Loss 1786 / Flat 2086) / skip 5677件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIN/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $1,044.12

## 4. Robust Adaptive DryRun ($100)

- 残高: **$230.42** / 初期 $100.00 (+130.42%)
- 確定: 3054件 (Win 839 / Loss 719 / Flat 1496) / skip 4990件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0186 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $230.42

## 5. Causal Adaptive DryRun ($100)

- 残高: **$124.71** / 初期 $100.00 (+24.71%)
- 確定: 2924件 (Win 869 / Loss 1142 / Flat 913) / pending 3件 / skip 3177件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000278 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SYN/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $124.71

## 6. Latest Market Context

- 更新: 2026-09-16T04:26:15.811128+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=75934.3
- Funnel: target 1064 → liquid 154 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +42.76% | $2,690,421.53 |
| ON/USDT:USDT | +19.33% | $3,158,718.31 |
| LSK/USDT:USDT | +14.29% | $17,291,897.94 |
| LONGXIA/USDT:USDT | +13.13% | $1,890,511.49 |
| USELESS/USDT:USDT | +11.69% | $5,046,102.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ON/USDT:USDT | below_1h_threshold | +3.48% | +3.29% |
| AKE/USDT:USDT | below_1h_threshold | +3.43% | +3.23% |
| BTW/USDT:USDT | below_1h_threshold | +3.02% | +2.82% |
| USELESS/USDT:USDT | below_1h_threshold | +1.84% | +1.65% |
| PYTH/USDT:USDT | below_1h_threshold | +1.71% | +1.52% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
