# Decision Report

- generated_at: 2026-08-17T17:26:24.112122+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11852**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11852, expectancy=-0.01%
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
| LIMIT_6PCT | 8/20 | 40.0% | +1.15% | **+0.46%** |
| LIMIT_BB3S | 9/12 | 75.0% | +0.58% | **+0.43%** |
| LIMIT_8PCT | 4/20 | 20.0% | +1.78% | **+0.36%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.67% | **+0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.85% | **+1.39%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.61% | **+0.97%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.95% | **+0.88%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.73% | **+0.78%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.76% | **+0.69%** |

## 2. $100 Live Portfolio

- 残高: **$121.53** / 初期 $100.00 (+21.53%)
- 確定トレード: 186件 (TP 72 / SL 109 / EXP 5)
- 最新: BR/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.53
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$614.71** / 初期 $100.00 (+514.71%)
- 確定: 4186件 (Win 1292 / Loss 1365 / Flat 1529) / skip 4227件
- 成長率目線: 平均log +0.000434 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TUT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $614.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.25** / 初期 $100.00 (+55.25%)
- 確定: 1818件 (Win 502 / Loss 427 / Flat 889) / skip 3445件
- 成長率目線: 平均log +0.000242 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0790 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AIO/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.12% 残高後 $155.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.53** / 初期 $100.00 (+17.53%)
- 確定: 1679件 (Win 504 / Loss 641 / Flat 534) / pending 0件 / skip 1647件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000190 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AIO/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $117.53

## 6. Latest Market Context

- 更新: 2026-08-17T17:26:15.616453+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=64198.5
- Funnel: target 992 → liquid 180 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TUT/USDT:USDT | +12.64% | $19,989,409.35 |
| ANSEM/USDT:USDT | +9.00% | $2,257,889.18 |
| HEMI/USDT:USDT | +4.09% | $2,192,451.15 |
| GIGGLE/USDT:USDT | +3.51% | $1,370,325.27 |
| HFT/USDT:USDT | +3.08% | $2,946,843.47 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONG/USDT:USDT | below_1h_threshold | +2.55% | +2.37% |
| SNXX/USDT:USDT | below_1h_threshold | +2.11% | +1.92% |
| AAOISTOCK/USDT:USDT | below_1h_threshold | +1.22% | +1.04% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +1.19% | +1.00% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +1.18% | +1.00% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
