# Decision Report

- generated_at: 2026-08-25T13:46:27.210468+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12605**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.38% / filled 20/20。**
- 全期間 MARKET基準: n=12605, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.38% | **+1.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.38% | **+1.38%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.69% | **+0.59%** |
| LIMIT_BB3S | 3/18 | 16.7% | +1.26% | **+0.21%** |
| LIMIT_2PCT | 13/20 | 65.0% | +0.18% | **+0.12%** |
| LIMIT_5PCT | 5/20 | 25.0% | -0.04% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +2.40% | **+1.44%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +1.45% | **+0.79%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.63% | **+0.41%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.45% | **+0.34%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +0.12% | **+0.08%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$687.36** / 初期 $100.00 (+587.36%)
- 確定: 4583件 (Win 1392 / Loss 1506 / Flat 1685) / skip 4583件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $687.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.51** / 初期 $100.00 (+55.51%)
- 確定: 1977件 (Win 536 / Loss 473 / Flat 968) / skip 4039件
- 成長率目線: 平均log +0.000223 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $155.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.66** / 初期 $100.00 (+14.66%)
- 確定: 1930件 (Win 564 / Loss 736 / Flat 630) / pending 4件 / skip 2144件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000041 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NES/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $114.66

## 6. Latest Market Context

- 更新: 2026-08-25T13:46:17.977706+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.60% price=78479.3
- Funnel: target 1023 → liquid 185 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +87.10% | $5,463,339.52 |
| JIMOTHY/USDT:USDT | +67.08% | $1,860,172.27 |
| ONG/USDT:USDT | +39.63% | $10,025,992.32 |
| TAC/USDT:USDT | +37.86% | $6,965,782.77 |
| BR/USDT:USDT | +18.53% | $3,812,157.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAC/USDT:USDT | below_1h_threshold | +3.83% | +4.42% |
| ACE/USDT:USDT | below_1h_threshold | +1.38% | +1.98% |
| AKE/USDT:USDT | below_1h_threshold | +1.36% | +1.96% |
| BR/USDT:USDT | below_1h_threshold | +1.12% | +1.72% |
| BLESS/USDT:USDT | below_1h_threshold | +1.05% | +1.65% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
