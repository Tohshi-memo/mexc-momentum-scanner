# Decision Report

- generated_at: 2026-08-02T11:36:33.395175+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10157**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.28% / filled 20/20。**
- 全期間 MARKET基準: n=10157, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.28% | **+1.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.28% | **+1.28%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +4.46% | **+1.11%** |
| LIMIT_BB3S | 3/19 | 15.8% | +6.66% | **+1.05%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.98% | **+0.88%** |
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +3.38% | **+0.84%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.36% | **+0.20%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.08% | **+0.02%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | -0.50% | **-0.20%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | -0.32% | **-0.21%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$566.31** / 初期 $100.00 (+466.31%)
- 確定: 3674件 (Win 1166 / Loss 1205 / Flat 1303) / skip 3044件
- 成長率目線: 平均log +0.000472 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $566.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.31** / 初期 $100.00 (+40.31%)
- 確定: 1281件 (Win 359 / Loss 298 / Flat 624) / skip 2287件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0085 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $140.31

## 5. Causal Adaptive DryRun ($100)

- 残高: **$112.42** / 初期 $100.00 (+12.42%)
- 確定: 963件 (Win 305 / Loss 376 / Flat 282) / pending 6件 / skip 662件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000217 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 1000RATS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $112.42

## 6. Latest Market Context

- 更新: 2026-08-02T11:36:17.865445+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=63146.4
- Funnel: target 922 → liquid 132 → pre 50 → checked 50 → surge 3 → strict 3
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLESS/USDT:USDT | +51.49% | $17,059,394.57 |
| HOME/USDT:USDT | +34.59% | $4,109,293.11 |
| UAI/USDT:USDT | +29.25% | $25,614,659.67 |
| 1000RATS/USDT:USDT | +27.02% | $33,494,559.93 |
| HYPER/USDT:USDT | +18.94% | $1,267,323.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HYPER/USDT:USDT | below_1h_threshold | +3.10% | +3.15% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.25% | +2.30% |
| KAITO/USDT:USDT | below_1h_threshold | +1.68% | +1.73% |
| HOME/USDT:USDT | below_1h_threshold | +1.38% | +1.43% |
| ADA/USDT:USDT | below_1h_threshold | +0.59% | +0.64% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
