# Decision Report

- generated_at: 2026-08-26T05:21:29.155948+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12664**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12664, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.58% | **-1.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 7/20 | 35.0% | +3.09% | **+1.08%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.08% | **+0.38%** |
| LIMIT_8PCT | 5/20 | 25.0% | +1.48% | **+0.37%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.79% | **+0.35%** |
| LIMIT_5PCT | 10/20 | 50.0% | -0.04% | **-0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +3.23% | **+2.75%** |
| MARKET_LONG | 20/20 | 100.0% | +2.58% | **+2.58%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +3.40% | **+2.04%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.95% | **+1.92%** |
| LIMIT_BB3S_LONG | 6/10 | 60.0% | +1.43% | **+0.86%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$687.36** / 初期 $100.00 (+587.36%)
- 確定: 4585件 (Win 1392 / Loss 1506 / Flat 1687) / skip 4640件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PONS/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $687.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.51** / 初期 $100.00 (+55.51%)
- 確定: 1978件 (Win 536 / Loss 473 / Flat 969) / skip 4097件
- 成長率目線: 平均log +0.000223 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0703 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BMT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $155.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.04** / 初期 $100.00 (+15.04%)
- 確定: 1941件 (Win 568 / Loss 741 / Flat 632) / pending 3件 / skip 2191件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000457 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTR/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $115.04

## 6. Latest Market Context

- 更新: 2026-08-26T05:21:19.408313+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=78725.0
- Funnel: target 1023 → liquid 166 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.4 >= 65=1, 4h RSI 86.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTR/USDT:USDT | +70.14% | $1,720,650.66 |
| BMT/USDT:USDT | +37.58% | $10,928,135.63 |
| PORTAL/USDT:USDT | +32.37% | $1,336,610.78 |
| LONGXIA/USDT:USDT | +25.11% | $1,867,745.98 |
| PONS/USDT:USDT | +24.38% | $1,134,906.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LONGXIA/USDT:USDT | below_1h_threshold | +1.98% | +2.06% |
| BICO/USDT:USDT | below_1h_threshold | +0.97% | +1.06% |
| STX/USDT:USDT | below_1h_threshold | +0.80% | +0.89% |
| FF/USDT:USDT | below_1h_threshold | +0.46% | +0.55% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.35% | +0.44% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
