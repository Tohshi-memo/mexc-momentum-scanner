# Decision Report

- generated_at: 2026-08-05T10:41:40.914741+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10394**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.76% / filled 20/20。**
- 全期間 MARKET基準: n=10394, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.76%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.76% | **+0.76%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 13/20 | 65.0% | +1.45% | **+0.94%** |
| LIMIT_BB3S | 5/19 | 26.3% | +2.94% | **+0.77%** |
| MARKET | 20/20 | 100.0% | +0.76% | **+0.76%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.80% | **+0.64%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.05% | **+0.51%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.73% | **+0.86%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.97% | **+0.59%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$605.31** / 初期 $100.00 (+505.31%)
- 確定: 3769件 (Win 1195 / Loss 1236 / Flat 1338) / skip 3186件
- 成長率目線: 平均log +0.000478 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $605.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$143.35** / 初期 $100.00 (+43.35%)
- 確定: 1316件 (Win 372 / Loss 310 / Flat 634) / skip 2489件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0577 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $143.35

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.16** / 初期 $100.00 (+18.16%)
- 確定: 1135件 (Win 364 / Loss 440 / Flat 331) / pending 6件 / skip 728件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000236 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $118.16

## 6. Latest Market Context

- 更新: 2026-08-05T10:41:30.709576+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=64203.1
- Funnel: target 945 → liquid 180 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.3 >= 65=1, 4h RSI 74.0 >= 65=1, 4h RSI 72.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLESS/USDT:USDT | +87.33% | $39,384,324.19 |
| HEI/USDT:USDT | +75.05% | $20,811,353.35 |
| HFT/USDT:USDT | +72.92% | $3,399,283.44 |
| BICO/USDT:USDT | +28.78% | $16,904,020.22 |
| GRVT/USDT:USDT | +28.60% | $7,004,885.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HFT/USDT:USDT | below_relative_strength | +5.10% | +4.98% |
| EVAA/USDT:USDT | below_1h_threshold | +4.49% | +4.37% |
| BLESS/USDT:USDT | below_1h_threshold | +3.07% | +2.95% |
| SKR/USDT:USDT | below_1h_threshold | +2.39% | +2.27% |
| KAITO/USDT:USDT | below_1h_threshold | +2.26% | +2.14% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
