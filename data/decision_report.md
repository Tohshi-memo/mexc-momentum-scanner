# Decision Report

- generated_at: 2026-08-14T06:56:31.829541+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11517**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11517, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.80% | **-0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 4/20 | 20.0% | +4.15% | **+0.83%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.23% | **+0.10%** |
| LIMIT_BB3S | 3/13 | 23.1% | +0.17% | **+0.04%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.79% | **+0.71%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.30% | **+0.22%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.19% | **+0.10%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.10% | **+0.04%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$604.23** / 初期 $100.00 (+504.23%)
- 確定: 3985件 (Win 1241 / Loss 1306 / Flat 1438) / skip 4093件
- 成長率目線: 平均log +0.000451 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AVAAI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $604.23

## 4. Robust Adaptive DryRun ($100)

- 残高: **$149.41** / 初期 $100.00 (+49.41%)
- 確定: 1651件 (Win 471 / Loss 398 / Flat 782) / skip 3277件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0795 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $149.41

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.45** / 初期 $100.00 (+16.45%)
- 確定: 1478件 (Win 437 / Loss 560 / Flat 481) / pending 2件 / skip 1506件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000210 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AVAAI/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $116.45

## 6. Latest Market Context

- 更新: 2026-08-14T06:56:21.468012+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.51% price=63034.0
- Funnel: target 981 → liquid 175 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.8 >= 65=1, 4h RSI 70.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +40.33% | $23,634,544.98 |
| EDEN/USDT:USDT | +27.60% | $33,325,747.32 |
| ACE/USDT:USDT | +24.62% | $4,063,930.70 |
| AKE/USDT:USDT | +22.19% | $60,444,174.43 |
| WDAYSTOCK/USDT:USDT | +18.43% | $1,571,185.37 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ACE/USDT:USDT | below_1h_threshold | +4.32% | +4.83% |
| HOME/USDT:USDT | below_1h_threshold | +1.71% | +2.22% |
| KORU/USDT:USDT | below_1h_threshold | +1.49% | +2.00% |
| GPS/USDT:USDT | below_1h_threshold | +1.44% | +1.95% |
| CAP/USDT:USDT | below_1h_threshold | +1.20% | +1.71% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
