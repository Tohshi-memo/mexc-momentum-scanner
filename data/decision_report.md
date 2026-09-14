# Decision Report

- generated_at: 2026-09-14T01:36:35.931746+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14477**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.69% / filled 20/20。**
- 全期間 MARKET基準: n=14477, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.69%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.69% | **+0.69%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.42% | **+1.35%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.01% | **+0.80%** |
| MARKET | 20/20 | 100.0% | +0.69% | **+0.69%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.74% | **+0.51%** |
| LIMIT_BB3S | 4/18 | 22.2% | +1.79% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| MARKET_LONG | 20/20 | 100.0% | +0.12% | **+0.12%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.19% | **+0.08%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | -0.03% | **-0.01%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -0.18% | **-0.04%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,072.66** / 初期 $100.00 (+972.66%)
- 確定: 5434件 (Win 1635 / Loss 1762 / Flat 2037) / skip 5604件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PUNDIX/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.22% 残高後 $1,072.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$227.62** / 初期 $100.00 (+127.62%)
- 確定: 2991件 (Win 830 / Loss 716 / Flat 1445) / skip 4897件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0686 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $227.62

## 5. Causal Adaptive DryRun ($100)

- 残高: **$126.71** / 初期 $100.00 (+26.71%)
- 確定: 2862件 (Win 851 / Loss 1107 / Flat 904) / pending 4件 / skip 3083件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000217 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: STEEM/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $126.71

## 6. Latest Market Context

- 更新: 2026-09-14T01:36:18.672781+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=76639.5
- Funnel: target 1068 → liquid 146 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 95.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +39.91% | $1,123,447.44 |
| POWER/USDT:USDT | +30.84% | $4,152,761.98 |
| BR/USDT:USDT | +7.51% | $2,307,659.94 |
| ARK/USDT:USDT | +7.40% | $3,136,152.22 |
| MAGMA/USDT:USDT | +5.15% | $1,811,401.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| POWR/USDT:USDT | below_1h_threshold | +4.07% | +4.24% |
| DELLSTOCK/USDT:USDT | below_1h_threshold | +1.28% | +1.46% |
| CHZ/USDT:USDT | below_1h_threshold | +1.08% | +1.26% |
| SOXS/USDT:USDT | below_1h_threshold | +1.07% | +1.24% |
| MAGMA/USDT:USDT | below_1h_threshold | +0.94% | +1.11% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
