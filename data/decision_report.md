# Decision Report

- generated_at: 2026-08-25T12:51:34.373689+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12601**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=12601, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.21% | **+0.06%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.06% | **+0.04%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.02% | **+0.01%** |
| LIMIT_6PCT | 2/20 | 10.0% | -1.06% | **-0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.36% | **+0.68%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.02% | **+0.61%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.00% | **+0.45%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.45% | **+0.34%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.38% | **+0.25%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$694.28** / 初期 $100.00 (+594.28%)
- 確定: 4581件 (Win 1392 / Loss 1504 / Flat 1685) / skip 4581件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $694.28

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.51** / 初期 $100.00 (+55.51%)
- 確定: 1977件 (Win 536 / Loss 473 / Flat 968) / skip 4035件
- 成長率目線: 平均log +0.000223 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $155.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.06** / 初期 $100.00 (+15.06%)
- 確定: 1928件 (Win 564 / Loss 734 / Flat 630) / pending 6件 / skip 2141件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000041 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $115.06

## 6. Latest Market Context

- 更新: 2026-08-25T12:51:22.778383+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=79035.3
- Funnel: target 1023 → liquid 180 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +93.85% | $5,172,879.24 |
| JIMOTHY/USDT:USDT | +74.83% | $1,739,231.82 |
| ONG/USDT:USDT | +41.10% | $9,398,534.74 |
| TAC/USDT:USDT | +32.56% | $6,835,876.55 |
| BR/USDT:USDT | +16.97% | $3,733,647.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HOLO/USDT:USDT | below_1h_threshold | +4.25% | +4.33% |
| JIMOTHY/USDT:USDT | below_1h_threshold | +2.92% | +3.00% |
| STORJ/USDT:USDT | below_1h_threshold | +2.61% | +2.69% |
| SPELL/USDT:USDT | below_1h_threshold | +1.56% | +1.64% |
| ETC/USDT:USDT | below_1h_threshold | +1.20% | +1.28% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
