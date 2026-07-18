# Decision Report

- generated_at: 2026-07-18T13:21:14.407892+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8947**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8947, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.27% | **-1.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_BB3S | 2/12 | 16.7% | +3.73% | **+0.62%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.23% | **+0.61%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.99% | **+0.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.24% | **+1.45%** |
| LIMIT_BB3S_LONG | 3/8 | 37.5% | +3.34% | **+1.25%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.08% | **+1.14%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.91% | **+1.05%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.60% | **+1.04%** |

## 2. $100 Live Portfolio

- 残高: **$110.69** / 初期 $100.00 (+10.69%)
- 確定トレード: 116件 (TP 43 / SL 69 / EXP 4)
- 最新: B/USDT:USDT SL_HIT PnL -3.30% 残高後 $110.69
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$358.77** / 初期 $100.00 (+258.77%)
- 確定: 3049件 (Win 946 / Loss 973 / Flat 1130) / skip 2459件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $358.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$112.48** / 初期 $100.00 (+12.48%)
- 確定: 908件 (Win 219 / Loss 184 / Flat 505) / skip 1450件
- 成長率目線: 平均log +0.000130 / 幾何平均 +0.013% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0657 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ROAM/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $112.48

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.72** / 初期 $100.00 (-1.28%)
- 確定: 193件 (Win 60 / Loss 106 / Flat 27) / pending 3件 / skip 224件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000209 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SYN/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $98.72

## 6. Latest Market Context

- 更新: 2026-07-18T13:21:07.726243+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.34% price=63961.2
- Funnel: target 885 → liquid 156 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +47.17% | $75,340,741.93 |
| XEC/USDT:USDT | +28.86% | $4,035,337.58 |
| B/USDT:USDT | +27.07% | $18,175,570.52 |
| TRADOOR/USDT:USDT | +25.97% | $5,344,909.92 |
| ALLO/USDT:USDT | +14.06% | $5,581,202.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +3.65% | +4.00% |
| DEXE/USDT:USDT | below_1h_threshold | +0.78% | +1.12% |
| ALLO/USDT:USDT | below_1h_threshold | +0.52% | +0.86% |
| UB/USDT:USDT | below_1h_threshold | +0.46% | +0.81% |
| TRB/USDT:USDT | below_1h_threshold | +0.38% | +0.73% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
