# Decision Report

- generated_at: 2026-08-17T14:51:46.756506+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11837**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11837, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.07%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.07% | **-1.07%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 9/20 | 45.0% | +2.42% | **+1.09%** |
| LIMIT_6PCT | 5/20 | 25.0% | +4.33% | **+1.08%** |
| LIMIT_BB3S | 4/15 | 26.7% | +3.50% | **+0.93%** |
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.87% | **+1.87%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.59% | **+1.19%** |
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +1.00% | **+1.00%** |
| MARKET_LONG | 20/20 | 100.0% | +0.86% | **+0.86%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.73% | **+0.78%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 185件 (TP 71 / SL 109 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$617.79** / 初期 $100.00 (+517.79%)
- 確定: 4185件 (Win 1292 / Loss 1364 / Flat 1529) / skip 4213件
- 成長率目線: 平均log +0.000435 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACE/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $617.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.25** / 初期 $100.00 (+55.25%)
- 確定: 1818件 (Win 502 / Loss 427 / Flat 889) / skip 3430件
- 成長率目線: 平均log +0.000242 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0044 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AIO/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.12% 残高後 $155.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.53** / 初期 $100.00 (+17.53%)
- 確定: 1679件 (Win 504 / Loss 641 / Flat 534) / pending 0件 / skip 1632件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000103 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AIO/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $117.53

## 6. Latest Market Context

- 更新: 2026-08-17T14:51:30.957215+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=63720.3
- Funnel: target 992 → liquid 178 → pre 50 → checked 50 → surge 5 → strict 1
- Surge前reject: below_1h_threshold=44, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.6 >= 65=1, 4h RSI 78.7 >= 65=1, 4h RSI 82.1 >= 65=1, 4h RSI 66.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIULAI/USDT:USDT | +130.10% | $5,181,791.44 |
| GPS/USDT:USDT | +47.34% | $23,773,506.42 |
| ACE/USDT:USDT | +37.45% | $30,645,880.77 |
| STAR/USDT:USDT | +33.37% | $1,000,929.31 |
| PORTAL/USDT:USDT | +21.87% | $16,674,039.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MRVLSTOCK/USDT:USDT | below_relative_strength | +5.11% | +4.99% |
| MUU/USDT:USDT | below_1h_threshold | +4.84% | +4.73% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +4.66% | +4.54% |
| ACE/USDT:USDT | below_1h_threshold | +4.27% | +4.16% |
| KORU/USDT:USDT | below_1h_threshold | +4.19% | +4.07% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
