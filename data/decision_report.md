# Decision Report

- generated_at: 2026-08-19T13:31:57.169643+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11974**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.34% / filled 20/20。**
- 全期間 MARKET基準: n=11974, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.34% | **+0.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.34% | **+0.34%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_5PCT | 2/20 | 10.0% | +0.95% | **+0.10%** |
| LIMIT_BB3S | 2/16 | 12.5% | +0.12% | **+0.02%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.72% | **+0.61%** |
| MARKET_LONG | 20/20 | 100.0% | +0.26% | **+0.26%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | -0.15% | **-0.08%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | -0.16% | **-0.10%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$623.96** / 初期 $100.00 (+523.96%)
- 確定: 4235件 (Win 1302 / Loss 1382 / Flat 1551) / skip 4300件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKHYNIXSTOCK/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.67% 残高後 $623.96

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.70** / 初期 $100.00 (+54.70%)
- 確定: 1821件 (Win 502 / Loss 428 / Flat 891) / skip 3564件
- 成長率目線: 平均log +0.000240 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $154.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.58** / 初期 $100.00 (+17.58%)
- 確定: 1750件 (Win 520 / Loss 666 / Flat 564) / pending 3件 / skip 1697件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000154 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $117.58

## 6. Latest Market Context

- 更新: 2026-08-19T13:31:34.154530+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.26% price=65027.8
- Funnel: target 997 → liquid 180 → pre 50 → checked 50 → surge 6 → strict 6
- Surge前reject: below_1h_threshold=44, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +68.67% | $104,437,719.80 |
| HEMI/USDT:USDT | +41.40% | $4,894,201.63 |
| STAR/USDT:USDT | +27.72% | $1,084,696.48 |
| UNITREE/USDT:USDT | +21.70% | $17,244,028.11 |
| MVLL/USDT:USDT | +21.06% | $5,106,998.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +4.68% | +4.42% |
| SKUU/USDT:USDT | below_1h_threshold | +3.84% | +3.58% |
| BTW/USDT:USDT | below_1h_threshold | +3.67% | +3.40% |
| NIULAI/USDT:USDT | below_1h_threshold | +2.81% | +2.55% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +2.77% | +2.50% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
