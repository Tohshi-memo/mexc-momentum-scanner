# Decision Report

- generated_at: 2026-09-17T13:11:27.511423+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14796**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.48% / filled 20/20。**
- 全期間 MARKET基準: n=14796, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.48% | **+2.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +3.11% | **+2.95%** |
| MARKET | 20/20 | 100.0% | +2.48% | **+2.48%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.42% | **+0.71%** |
| LIMIT_BB3S | 2/17 | 11.8% | +2.00% | **+0.24%** |
| LIMIT_2PCT | 13/20 | 65.0% | +0.32% | **+0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.67% | **+0.73%** |
| LIMIT_7PCT_LONG | 12/20 | 60.0% | +0.67% | **+0.40%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.44% | **+0.20%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.08% | **+0.05%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,159.77** / 初期 $100.00 (+1059.77%)
- 確定: 5602件 (Win 1679 / Loss 1814 / Flat 2109) / skip 5755件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GENIUS/USDT:USDT `LIMIT_7PCT_LONG` SL_HIT account -0.50% 残高後 $1,159.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$239.89** / 初期 $100.00 (+139.89%)
- 確定: 3130件 (Win 870 / Loss 747 / Flat 1513) / skip 5077件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0948 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BATON/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $239.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.53** / 初期 $100.00 (+23.53%)
- 確定: 2958件 (Win 878 / Loss 1165 / Flat 915) / pending 0件 / skip 3312件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000199 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $123.53

## 6. Latest Market Context

- 更新: 2026-09-17T13:11:14.011916+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=76628.3
- Funnel: target 1050 → liquid 159 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AVA/USDT:USDT | +96.18% | $3,403,237.20 |
| ONE/USDT:USDT | +61.92% | $11,451,555.79 |
| BATON/USDT:USDT | +36.65% | $2,551,336.80 |
| GENIUS/USDT:USDT | +31.91% | $1,687,352.33 |
| MARSCOIN/USDT:USDT | +21.44% | $3,036,624.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PONS/USDT:USDT | below_1h_threshold | +4.61% | +4.70% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +3.84% | +3.93% |
| MVLL/USDT:USDT | below_1h_threshold | +2.70% | +2.80% |
| HNT/USDT:USDT | below_1h_threshold | +1.57% | +1.67% |
| LIT/USDT:USDT | below_1h_threshold | +1.27% | +1.36% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
