# Decision Report

- generated_at: 2026-08-18T00:46:29.156476+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11864**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.88% / filled 20/20。**
- 全期間 MARKET基準: n=11864, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.80% | **+0.70%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.81% | **+0.57%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.65% | **+0.55%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.67% | **+0.50%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.69% | **+0.38%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.37% | **+0.22%** |
| LIMIT_BB3S_LONG | 6/8 | 75.0% | +0.28% | **+0.21%** |

## 2. $100 Live Portfolio

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定トレード: 187件 (TP 72 / SL 110 / EXP 5)
- 最新: HEMI/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.41
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$611.63** / 初期 $100.00 (+511.63%)
- 確定: 4187件 (Win 1292 / Loss 1366 / Flat 1529) / skip 4238件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIULAI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $611.63

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.25** / 初期 $100.00 (+55.25%)
- 確定: 1819件 (Win 502 / Loss 427 / Flat 890) / skip 3456件
- 成長率目線: 平均log +0.000242 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0714 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $155.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.53** / 初期 $100.00 (+17.53%)
- 確定: 1679件 (Win 504 / Loss 641 / Flat 534) / pending 1件 / skip 1656件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000166 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AIO/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $117.53

## 6. Latest Market Context

- 更新: 2026-08-18T00:46:18.769638+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.21% price=64368.4
- Funnel: target 992 → liquid 177 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PIEVERSE/USDT:USDT | +15.38% | $1,223,363.79 |
| BEAT/USDT:USDT | +8.99% | $30,319,941.45 |
| ANSEM/USDT:USDT | +8.05% | $3,859,490.91 |
| COMP/USDT:USDT | +7.63% | $3,041,044.95 |
| ALLO/USDT:USDT | +7.45% | $8,302,216.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIEVERSE/USDT:USDT | below_1h_threshold | +3.66% | +3.88% |
| TUT/USDT:USDT | below_1h_threshold | +2.59% | +2.80% |
| US/USDT:USDT | below_1h_threshold | +2.54% | +2.75% |
| ANSEM/USDT:USDT | below_1h_threshold | +1.39% | +1.60% |
| DIA/USDT:USDT | below_1h_threshold | +1.26% | +1.48% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
