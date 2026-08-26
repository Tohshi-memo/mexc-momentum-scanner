# Decision Report

- generated_at: 2026-08-26T13:51:38.053944+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12713**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.04% / filled 20/20。**
- 全期間 MARKET基準: n=12713, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.04%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.04% | **+1.04%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.04% | **+1.04%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.84% | **+0.79%** |
| LIMIT_BB3S | 9/15 | 60.0% | +1.10% | **+0.66%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.70% | **+0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.59% | **+0.56%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.33% | **+0.26%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | -0.03% | **-0.01%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$690.03** / 初期 $100.00 (+590.03%)
- 確定: 4612件 (Win 1400 / Loss 1516 / Flat 1696) / skip 4662件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TAC/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $690.03

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.51** / 初期 $100.00 (+56.51%)
- 確定: 2001件 (Win 544 / Loss 483 / Flat 974) / skip 4123件
- 成長率目線: 平均log +0.000224 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0714 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BICO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $156.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.00** / 初期 $100.00 (+16.00%)
- 確定: 1980件 (Win 580 / Loss 756 / Flat 644) / pending 2件 / skip 2205件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000214 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONG/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.00

## 6. Latest Market Context

- 更新: 2026-08-26T13:51:24.197732+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=78282.3
- Funnel: target 1023 → liquid 167 → pre 50 → checked 50 → surge 5 → strict 1
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.3 >= 65=1, 4h RSI 83.7 >= 65=1, 4h RSI 95.8 >= 65=1, 4h RSI 68.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTR/USDT:USDT | +304.64% | $20,720,194.35 |
| TAC/USDT:USDT | +73.72% | $8,951,515.58 |
| BMT/USDT:USDT | +53.56% | $16,580,866.43 |
| LONGXIA/USDT:USDT | +45.19% | $2,017,346.10 |
| ONG/USDT:USDT | +29.20% | $11,457,623.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONT/USDT:USDT | below_1h_threshold | +3.68% | +3.68% |
| BMT/USDT:USDT | below_1h_threshold | +3.28% | +3.28% |
| BR/USDT:USDT | below_1h_threshold | +2.75% | +2.74% |
| METASTOCK/USDT:USDT | below_1h_threshold | +2.27% | +2.27% |
| SOXS/USDT:USDT | below_1h_threshold | +1.91% | +1.90% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
