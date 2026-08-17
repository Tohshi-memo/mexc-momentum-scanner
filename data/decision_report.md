# Decision Report

- generated_at: 2026-08-17T16:51:46.164585+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11847**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11847, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.82% | **-0.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 7/20 | 35.0% | +1.83% | **+0.64%** |
| LIMIT_BB3S | 7/15 | 46.7% | +1.24% | **+0.58%** |
| LIMIT_8PCT | 5/20 | 25.0% | +2.16% | **+0.54%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.95% | **+0.52%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.15% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +1.45% | **+1.16%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.27% | **+1.14%** |
| MARKET_LONG | 20/20 | 100.0% | +1.04% | **+1.04%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.40% | **+0.91%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.49% | **+0.87%** |

## 2. $100 Live Portfolio

- 残高: **$121.53** / 初期 $100.00 (+21.53%)
- 確定トレード: 186件 (TP 72 / SL 109 / EXP 5)
- 最新: BR/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.53
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$617.79** / 初期 $100.00 (+517.79%)
- 確定: 4185件 (Win 1292 / Loss 1364 / Flat 1529) / skip 4223件
- 成長率目線: 平均log +0.000435 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACE/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $617.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.25** / 初期 $100.00 (+55.25%)
- 確定: 1818件 (Win 502 / Loss 427 / Flat 889) / skip 3440件
- 成長率目線: 平均log +0.000242 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0781 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AIO/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.12% 残高後 $155.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.53** / 初期 $100.00 (+17.53%)
- 確定: 1679件 (Win 504 / Loss 641 / Flat 534) / pending 0件 / skip 1646件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000128 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AIO/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $117.53

## 6. Latest Market Context

- 更新: 2026-08-17T16:51:32.529835+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=64072.9
- Funnel: target 992 → liquid 180 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.5 >= 65=1, 4h RSI 75.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TUT/USDT:USDT | +20.98% | $15,851,919.30 |
| ANSEM/USDT:USDT | +20.66% | $1,921,314.13 |
| GPS/USDT:USDT | +5.26% | $27,956,939.06 |
| HFT/USDT:USDT | +4.69% | $2,848,643.98 |
| HEMI/USDT:USDT | +3.65% | $2,265,425.82 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HFT/USDT:USDT | below_1h_threshold | +4.83% | +4.98% |
| HEMI/USDT:USDT | below_1h_threshold | +3.53% | +3.68% |
| CRV/USDT:USDT | below_1h_threshold | +3.06% | +3.21% |
| FHE/USDT:USDT | below_1h_threshold | +2.77% | +2.92% |
| DOS/USDT:USDT | below_1h_threshold | +2.58% | +2.73% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
