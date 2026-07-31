# Decision Report

- generated_at: 2026-07-31T02:21:25.662407+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9949**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9949, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.92% | **-0.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 15/20 | 75.0% | +0.68% | **+0.51%** |
| LIMIT_5PCT | 4/20 | 20.0% | +1.48% | **+0.30%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.23% | **+0.19%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.45% | **+0.14%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +2.75% | **+2.75%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +3.37% | **+2.36%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.27% | **+1.48%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.52% | **+1.44%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.44% | **+1.34%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$536.70** / 初期 $100.00 (+436.70%)
- 確定: 3540件 (Win 1127 / Loss 1152 / Flat 1261) / skip 2970件
- 成長率目線: 平均log +0.000475 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KOMA/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $536.70

## 4. Robust Adaptive DryRun ($100)

- 残高: **$139.04** / 初期 $100.00 (+39.04%)
- 確定: 1246件 (Win 347 / Loss 283 / Flat 616) / skip 2114件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2213 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $139.04

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.57** / 初期 $100.00 (+10.57%)
- 確定: 805件 (Win 262 / Loss 320 / Flat 223) / pending 0件 / skip 621件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000655 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ARMSTOCK/USDT:USDT `MARKET` EXPIRED account -0.04% 残高後 $110.57

## 6. Latest Market Context

- 更新: 2026-07-31T02:21:16.442372+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.20% price=64406.3
- Funnel: target 920 → liquid 169 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AXTISTOCK/USDT:USDT | +27.91% | $3,745,818.54 |
| MMT/USDT:USDT | +25.64% | $9,344,168.50 |
| AMZU/USDT:USDT | +16.65% | $1,944,577.97 |
| ZHIPUSTOCK/USDT:USDT | +16.22% | $5,579,289.02 |
| ADVANTESTSTOCK/USDT:USDT | +14.67% | $1,612,650.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GRVT/USDT:USDT | below_1h_threshold | +2.59% | +2.79% |
| GIGGLE/USDT:USDT | below_1h_threshold | +2.47% | +2.67% |
| MMT/USDT:USDT | below_1h_threshold | +2.41% | +2.61% |
| AKE/USDT:USDT | below_1h_threshold | +2.22% | +2.42% |
| CAP/USDT:USDT | below_1h_threshold | +2.16% | +2.36% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
