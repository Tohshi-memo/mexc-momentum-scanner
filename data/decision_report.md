# Decision Report

- generated_at: 2026-08-01T00:56:25.091879+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10039**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.34% / filled 20/20。**
- 全期間 MARKET基準: n=10039, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.34% | **+0.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +0.83% | **+0.79%** |
| LIMIT_BB3S | 5/20 | 25.0% | +2.81% | **+0.70%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.48% | **+0.62%** |
| MARKET | 20/20 | 100.0% | +0.34% | **+0.34%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.20% | **+0.84%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.53% | **+0.84%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.77% | **+0.73%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.86% | **+0.69%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$572.88** / 初期 $100.00 (+472.88%)
- 確定: 3591件 (Win 1149 / Loss 1173 / Flat 1269) / skip 3009件
- 成長率目線: 平均log +0.000486 / 幾何平均 +0.049% per trade / maxDD +8.13%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_3PCT_LONG` TP_HIT account +1.00% 残高後 $572.88

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1279件 (Win 359 / Loss 297 / Flat 623) / skip 2171件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0016 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$111.97** / 初期 $100.00 (+11.97%)
- 確定: 863件 (Win 280 / Loss 341 / Flat 242) / pending 5件 / skip 648件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000278 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $111.97

## 6. Latest Market Context

- 更新: 2026-08-01T00:56:15.205451+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=62942.5
- Funnel: target 921 → liquid 172 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 96.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KOMA/USDT:USDT | +29.73% | $17,763,054.40 |
| GIGGLE/USDT:USDT | +24.45% | $21,657,596.14 |
| JIMOTHY/USDT:USDT | +22.78% | $1,168,491.58 |
| 1000RATS/USDT:USDT | +21.97% | $17,351,612.09 |
| BTW/USDT:USDT | +15.42% | $1,884,153.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SHIB/USDT:USDT | below_1h_threshold | +4.29% | +4.16% |
| CAP/USDT:USDT | below_1h_threshold | +3.25% | +3.12% |
| ORDI/USDT:USDT | below_1h_threshold | +2.91% | +2.78% |
| GIGGLE/USDT:USDT | below_1h_threshold | +2.33% | +2.20% |
| USELESS/USDT:USDT | below_1h_threshold | +2.11% | +1.98% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
