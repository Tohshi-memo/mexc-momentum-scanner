# Decision Report

- generated_at: 2026-08-25T13:26:34.827588+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12603**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.78% / filled 20/20。**
- 全期間 MARKET基準: n=12603, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.78% | **+0.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.78% | **+0.78%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.05% | **+0.04%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.03% | **+0.02%** |
| LIMIT_5PCT | 5/20 | 25.0% | -0.04% | **-0.01%** |
| LIMIT_6PCT | 2/20 | 10.0% | -1.06% | **-0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.41% | **+1.20%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.56% | **+1.01%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.70% | **+0.85%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.45% | **+0.34%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.39% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$687.36** / 初期 $100.00 (+587.36%)
- 確定: 4583件 (Win 1392 / Loss 1506 / Flat 1685) / skip 4581件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $687.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.51** / 初期 $100.00 (+55.51%)
- 確定: 1977件 (Win 536 / Loss 473 / Flat 968) / skip 4037件
- 成長率目線: 平均log +0.000223 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $155.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.86** / 初期 $100.00 (+14.86%)
- 確定: 1929件 (Win 564 / Loss 735 / Flat 630) / pending 5件 / skip 2143件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000036 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONG/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $114.86

## 6. Latest Market Context

- 更新: 2026-08-25T13:26:21.879970+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.27% price=78740.7
- Funnel: target 1023 → liquid 181 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +91.47% | $5,367,742.37 |
| JIMOTHY/USDT:USDT | +67.28% | $1,823,741.39 |
| ONG/USDT:USDT | +41.33% | $9,864,242.22 |
| TAC/USDT:USDT | +34.59% | $6,911,411.71 |
| BR/USDT:USDT | +17.85% | $3,782,177.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONT/USDT:USDT | below_1h_threshold | +1.61% | +1.88% |
| TAC/USDT:USDT | below_1h_threshold | +1.40% | +1.67% |
| ACE/USDT:USDT | below_1h_threshold | +1.16% | +1.42% |
| POPCAT/USDT:USDT | below_1h_threshold | +0.88% | +1.14% |
| BLESS/USDT:USDT | below_1h_threshold | +0.75% | +1.02% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
