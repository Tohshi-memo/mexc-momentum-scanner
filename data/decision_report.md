# Decision Report

- generated_at: 2026-07-31T02:31:25.816308+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9950**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9950, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.92% | **-0.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 15/20 | 75.0% | +0.54% | **+0.41%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.37% | **+0.34%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.51% | **+0.18%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.17% | **+0.14%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +3.19% | **+2.07%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +3.69% | **+1.29%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.32% | **+1.19%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.95% | **+1.17%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.97% | **+0.98%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$536.70** / 初期 $100.00 (+436.70%)
- 確定: 3541件 (Win 1127 / Loss 1152 / Flat 1262) / skip 2970件
- 成長率目線: 平均log +0.000475 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KOMA/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $536.70

## 4. Robust Adaptive DryRun ($100)

- 残高: **$139.04** / 初期 $100.00 (+39.04%)
- 確定: 1247件 (Win 347 / Loss 283 / Flat 617) / skip 2114件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2155 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $139.04

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.57** / 初期 $100.00 (+10.57%)
- 確定: 805件 (Win 262 / Loss 320 / Flat 223) / pending 0件 / skip 623件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000658 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ARMSTOCK/USDT:USDT `MARKET` EXPIRED account -0.04% 残高後 $110.57

## 6. Latest Market Context

- 更新: 2026-07-31T02:31:17.636894+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.28% price=64355.3
- Funnel: target 920 → liquid 170 → pre 50 → checked 50 → surge 4 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AXTISTOCK/USDT:USDT | +28.16% | $3,770,353.27 |
| MMT/USDT:USDT | +28.00% | $9,474,050.92 |
| GRVT/USDT:USDT | +26.34% | $1,344,796.52 |
| AMZU/USDT:USDT | +17.07% | $1,947,036.55 |
| ADVANTESTSTOCK/USDT:USDT | +14.41% | $1,613,743.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MMT/USDT:USDT | below_1h_threshold | +4.60% | +4.88% |
| AKE/USDT:USDT | below_1h_threshold | +2.40% | +2.68% |
| GIGGLE/USDT:USDT | below_1h_threshold | +2.33% | +2.61% |
| QXOSTOCK/USDT:USDT | below_1h_threshold | +1.30% | +1.58% |
| TESLA/USDT:USDT | below_1h_threshold | +1.23% | +1.51% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
