# Decision Report

- generated_at: 2026-11-13T06:26:28.595471+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18789**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.61% / filled 20/20。**
- 全期間 MARKET基準: n=18789, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.61%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.61% | **+0.61%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.42% | **+1.35%** |
| LIMIT_6PCT | 7/20 | 35.0% | +2.79% | **+0.98%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.00% | **+0.85%** |
| LIMIT_9PCT | 4/20 | 20.0% | +4.15% | **+0.83%** |
| LIMIT_8PCT | 5/20 | 25.0% | +3.02% | **+0.76%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +2.56% | **+1.54%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.99% | **+1.49%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +1.53% | **+1.37%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.00% | **+1.33%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.23% | **+1.17%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 273件 (TP 99 / SL 166 / EXP 8)
- 最新: IDOL/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,754.62** / 初期 $100.00 (+1654.62%)
- 確定: 7259件 (Win 2092 / Loss 2325 / Flat 2842) / skip 8091件
- 成長率目線: 平均log +0.000395 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,754.62

## 4. Robust Adaptive DryRun ($100)

- 残高: **$402.19** / 初期 $100.00 (+302.19%)
- 確定: 4808件 (Win 1296 / Loss 1067 / Flat 2445) / skip 7392件
- 成長率目線: 平均log +0.000289 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0645 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $402.19

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6949件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000199 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-13T06:26:15.186057+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.94% price=68755.6
- Funnel: target 1105 → liquid 152 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BARD/USDT:USDT | +46.95% | $10,746,958.64 |
| KOR/USDT:USDT | +44.84% | $1,721,821.33 |
| ARIA/USDT:USDT | +36.32% | $9,397,631.05 |
| AKE/USDT:USDT | +34.74% | $9,027,016.94 |
| GANG/USDT:USDT | +18.05% | $1,181,679.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_relative_strength | +5.67% | +4.72% |
| UAI/USDT:USDT | below_1h_threshold | +4.31% | +3.36% |
| Q/USDT:USDT | below_1h_threshold | +3.68% | +2.74% |
| PONS/USDT:USDT | below_1h_threshold | +3.60% | +2.65% |
| ZRO/USDT:USDT | below_1h_threshold | +3.27% | +2.33% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
