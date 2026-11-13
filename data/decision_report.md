# Decision Report

- generated_at: 2026-11-13T06:36:26.372323+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18790**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18790, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.01% | **+0.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +2.79% | **+0.98%** |
| LIMIT_9PCT | 4/20 | 20.0% | +4.15% | **+0.83%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.84% | **+0.80%** |
| LIMIT_8PCT | 5/20 | 25.0% | +3.02% | **+0.76%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.84% | **+0.75%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +2.09% | **+1.88%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +3.16% | **+1.74%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +2.42% | **+1.69%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.71% | **+1.62%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.55% | **+1.08%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 273件 (TP 99 / SL 166 / EXP 8)
- 最新: IDOL/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,754.62** / 初期 $100.00 (+1654.62%)
- 確定: 7260件 (Win 2092 / Loss 2325 / Flat 2843) / skip 8091件
- 成長率目線: 平均log +0.000395 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $1,754.62

## 4. Robust Adaptive DryRun ($100)

- 残高: **$403.91** / 初期 $100.00 (+303.91%)
- 確定: 4809件 (Win 1297 / Loss 1067 / Flat 2445) / skip 7392件
- 成長率目線: 平均log +0.000290 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0594 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $403.91

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6950件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000165 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-13T06:36:14.845340+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +1.09% price=68858.4
- Funnel: target 1105 → liquid 153 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BARD/USDT:USDT | +46.95% | $10,811,960.55 |
| KOR/USDT:USDT | +39.69% | $1,730,441.49 |
| ARIA/USDT:USDT | +38.07% | $9,437,511.93 |
| AKE/USDT:USDT | +29.79% | $9,267,594.89 |
| GANG/USDT:USDT | +13.16% | $1,190,107.70 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZRO/USDT:USDT | below_1h_threshold | +4.56% | +3.46% |
| PONS/USDT:USDT | below_1h_threshold | +4.39% | +3.30% |
| UAI/USDT:USDT | below_1h_threshold | +4.36% | +3.27% |
| H/USDT:USDT | below_1h_threshold | +3.43% | +2.33% |
| NEAR/USDT:USDT | below_1h_threshold | +3.39% | +2.29% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
