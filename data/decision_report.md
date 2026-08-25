# Decision Report

- generated_at: 2026-08-25T15:06:41.773678+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12610**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.02% / filled 20/20。**
- 全期間 MARKET基準: n=12610, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.02% | **+2.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.02% | **+2.02%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.94% | **+0.75%** |
| LIMIT_BB3S | 3/17 | 17.6% | +1.26% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +1.54% | **+0.92%** |
| LIMIT_7PCT_LONG | 12/20 | 60.0% | +1.01% | **+0.61%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.48% | **+0.25%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.35% | **+0.14%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.10% | **+0.05%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$687.36** / 初期 $100.00 (+587.36%)
- 確定: 4583件 (Win 1392 / Loss 1506 / Flat 1685) / skip 4588件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $687.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.51** / 初期 $100.00 (+55.51%)
- 確定: 1977件 (Win 536 / Loss 473 / Flat 968) / skip 4044件
- 成長率目線: 平均log +0.000223 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $155.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.46** / 初期 $100.00 (+14.46%)
- 確定: 1931件 (Win 564 / Loss 737 / Flat 630) / pending 3件 / skip 2154件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000035 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: POPCAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $114.46

## 6. Latest Market Context

- 更新: 2026-08-25T15:06:30.958397+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=79192.5
- Funnel: target 1023 → liquid 182 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.6 >= 65=1, 4h RSI 88.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +88.17% | $5,692,076.08 |
| AGI/USDT:USDT | +63.70% | $1,064,509.04 |
| JIMOTHY/USDT:USDT | +60.07% | $2,129,318.09 |
| TAC/USDT:USDT | +40.80% | $7,367,884.75 |
| ONG/USDT:USDT | +39.02% | $11,081,553.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SPX/USDT:USDT | below_1h_threshold | +2.36% | +2.37% |
| ACE/USDT:USDT | below_1h_threshold | +1.69% | +1.70% |
| RCATSTOCK/USDT:USDT | below_1h_threshold | +1.03% | +1.04% |
| JASMY/USDT:USDT | below_1h_threshold | +0.92% | +0.93% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +0.78% | +0.78% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
