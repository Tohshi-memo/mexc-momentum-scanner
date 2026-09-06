# Decision Report

- generated_at: 2026-09-06T16:41:35.356438+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13825**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.22% / filled 20/20。**
- 全期間 MARKET基準: n=13825, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.22% | **+2.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +2.83% | **+2.54%** |
| MARKET | 20/20 | 100.0% | +2.22% | **+2.22%** |
| LIMIT_ATR | 10/20 | 50.0% | +2.75% | **+1.37%** |
| LIMIT_3PCT | 12/20 | 60.0% | +2.02% | **+1.21%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +3.44% | **+1.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.65% | **+0.33%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +0.67% | **+0.13%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +0.37% | **+0.13%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | -0.44% | **-0.20%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | -0.68% | **-0.41%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$837.19** / 初期 $100.00 (+737.19%)
- 確定: 5127件 (Win 1538 / Loss 1680 / Flat 1909) / skip 5259件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $837.19

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.84** / 初期 $100.00 (+88.84%)
- 確定: 2569件 (Win 717 / Loss 617 / Flat 1235) / skip 4667件
- 成長率目線: 平均log +0.000247 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0102 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $188.84

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.85** / 初期 $100.00 (+18.85%)
- 確定: 2436件 (Win 724 / Loss 930 / Flat 782) / pending 6件 / skip 2856件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000162 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $118.85

## 6. Latest Market Context

- 更新: 2026-09-06T16:41:16.111323+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=79697.8
- Funnel: target 1059 → liquid 127 → pre 50 → checked 50 → surge 4 → strict 3
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 4/USDT:USDT | +7.65% | $13,985,129.61 |
| BASECAT/USDT:USDT | +6.91% | $2,247,399.05 |
| USELESS/USDT:USDT | +5.45% | $17,590,411.80 |
| 1000BONK/USDT:USDT | +5.11% | $4,980,792.49 |
| UNI/USDT:USDT | +4.97% | $58,145,893.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UNI/USDT:USDT | below_1h_threshold | +4.88% | +4.85% |
| UAI/USDT:USDT | below_1h_threshold | +4.11% | +4.08% |
| SUSHI/USDT:USDT | below_1h_threshold | +3.44% | +3.42% |
| DASH/USDT:USDT | below_1h_threshold | +3.26% | +3.24% |
| BULLA/USDT:USDT | below_1h_threshold | +2.94% | +2.92% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
