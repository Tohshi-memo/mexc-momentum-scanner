# Decision Report

- generated_at: 2026-11-16T02:56:33.343374+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18993**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.15% / filled 20/20。**
- 全期間 MARKET基準: n=18993, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.15%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.15% | **+1.15%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.15% | **+1.15%** |
| LIMIT_BB3S | 2/11 | 18.2% | +3.02% | **+0.55%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.09% | **+0.41%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.34% | **+0.24%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.66% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 15/20 | 75.0% | +1.17% | **+0.87%** |
| LIMIT_BB3S_LONG | 4/9 | 44.4% | +1.07% | **+0.48%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +0.47% | **+0.31%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.24% | **+0.17%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +0.44% | **+0.09%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 276件 (TP 100 / SL 168 / EXP 8)
- 最新: IDOL/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,703.15** / 初期 $100.00 (+1603.15%)
- 確定: 7336件 (Win 2106 / Loss 2349 / Flat 2881) / skip 8218件
- 成長率目線: 平均log +0.000386 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BARD/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,703.15

## 4. Robust Adaptive DryRun ($100)

- 残高: **$429.80** / 初期 $100.00 (+329.80%)
- 確定: 4981件 (Win 1331 / Loss 1081 / Flat 2569) / skip 7423件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0058 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BARD/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $429.80

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7154件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000095 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-16T02:56:18.978349+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.82% price=65067.7
- Funnel: target 1066 → liquid 114 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RARE/USDT:USDT | +46.24% | $5,730,479.58 |
| SHELL/USDT:USDT | +13.79% | $1,625,027.92 |
| BARD/USDT:USDT | +7.33% | $1,860,540.22 |
| MSTRSTOCK/USDT:USDT | +4.78% | $8,481,966.38 |
| PIEVERSE/USDT:USDT | +4.50% | $2,111,213.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JCT/USDT:USDT | below_1h_threshold | +2.52% | +1.70% |
| ICP/USDT:USDT | below_1h_threshold | +2.45% | +1.63% |
| NEAR/USDT:USDT | below_1h_threshold | +2.40% | +1.57% |
| APT/USDT:USDT | below_1h_threshold | +2.36% | +1.54% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +2.31% | +1.49% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
