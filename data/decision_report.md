# Decision Report

- generated_at: 2026-10-29T02:16:26.851136+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17748**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.62% / filled 20/20。**
- 全期間 MARKET基準: n=17748, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.62%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.62% | **+1.62%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.62% | **+1.62%** |
| LIMIT_BB3S | 6/20 | 30.0% | +4.07% | **+1.22%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.95% | **+0.76%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.30% | **+0.25%** |
| MARKET_LONG | 20/20 | 100.0% | +0.19% | **+0.19%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -0.27% | **-0.05%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 255件 (TP 94 / SL 153 / EXP 8)
- 最新: BTW/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,545.23** / 初期 $100.00 (+1445.23%)
- 確定: 6792件 (Win 1971 / Loss 2173 / Flat 2648) / skip 7517件
- 成長率目線: 平均log +0.000403 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COHRSTOCK/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,545.23

## 4. Robust Adaptive DryRun ($100)

- 残高: **$358.73** / 初期 $100.00 (+258.73%)
- 確定: 4269件 (Win 1155 / Loss 971 / Flat 2143) / skip 6890件
- 成長率目線: 平均log +0.000299 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0118 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: COHRSTOCK/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $358.73

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5909件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000280 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-29T02:16:11.732480+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=79903.9
- Funnel: target 1083 → liquid 172 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IDOL/USDT:USDT | +56.98% | $1,948,766.95 |
| INIT/USDT:USDT | +11.55% | $2,111,920.51 |
| Q/USDT:USDT | +10.10% | $30,627,525.78 |
| AKE/USDT:USDT | +7.61% | $6,842,958.99 |
| ORCLSTOCK/USDT:USDT | +6.78% | $5,135,623.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| Q/USDT:USDT | below_1h_threshold | +3.90% | +3.98% |
| CAP/USDT:USDT | below_1h_threshold | +3.72% | +3.81% |
| SKDD/USDT:USDT | below_1h_threshold | +3.01% | +3.09% |
| UNITREE/USDT:USDT | below_1h_threshold | +2.90% | +2.99% |
| SOXS/USDT:USDT | below_1h_threshold | +2.58% | +2.66% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
