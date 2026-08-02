# Decision Report

- generated_at: 2026-08-02T13:51:21.288689+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10162**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.08% / filled 20/20。**
- 全期間 MARKET基準: n=10162, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+3.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.08% | **+3.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.08% | **+3.08%** |
| LIMIT_1PCT | 18/20 | 90.0% | +2.87% | **+2.58%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +4.06% | **+1.42%** |
| LIMIT_2PCT | 11/20 | 55.0% | +2.38% | **+1.31%** |
| LIMIT_3PCT | 9/20 | 45.0% | +1.68% | **+0.76%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +3.38% | **+0.84%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +0.36% | **+0.20%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.08% | **+0.02%** |
| LIMIT_4PCT_LONG | 15/20 | 75.0% | -0.00% | **-0.00%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | -0.13% | **-0.04%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$566.31** / 初期 $100.00 (+466.31%)
- 確定: 3674件 (Win 1166 / Loss 1205 / Flat 1303) / skip 3049件
- 成長率目線: 平均log +0.000472 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $566.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.31** / 初期 $100.00 (+40.31%)
- 確定: 1281件 (Win 359 / Loss 298 / Flat 624) / skip 2292件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0150 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $140.31

## 5. Causal Adaptive DryRun ($100)

- 残高: **$112.32** / 初期 $100.00 (+12.32%)
- 確定: 966件 (Win 306 / Loss 378 / Flat 282) / pending 3件 / skip 665件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000127 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CAP/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $112.32

## 6. Latest Market Context

- 更新: 2026-08-02T13:51:13.306042+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=63103.1
- Funnel: target 922 → liquid 135 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.6 >= 65=1, 4h RSI 93.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLESS/USDT:USDT | +64.24% | $21,245,906.31 |
| HOME/USDT:USDT | +30.49% | $4,719,496.06 |
| UAI/USDT:USDT | +24.82% | $27,844,435.26 |
| MANTRA/USDT:USDT | +18.78% | $1,498,622.80 |
| HYPER/USDT:USDT | +17.50% | $1,789,206.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIL/USDT:USDT | below_1h_threshold | +4.24% | +4.23% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.43% | +2.42% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.14% | +2.13% |
| INJ/USDT:USDT | below_1h_threshold | +0.83% | +0.82% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +0.77% | +0.76% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
