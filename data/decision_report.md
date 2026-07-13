# Decision Report

- generated_at: 2026-07-13T17:36:19.323948+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8646**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8646, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +2.91% | **+0.87%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.74% | **+0.78%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_FIB1618 | 5/20 | 25.0% | +0.85% | **+0.21%** |
| LIMIT_BB3S | 4/20 | 20.0% | +0.02% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +3.66% | **+2.19%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +3.94% | **+1.97%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.80% | **+1.68%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +4.69% | **+1.64%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.50% | **+1.27%** |

## 2. $100 Live Portfolio

- 残高: **$101.19** / 初期 $100.00 (+1.19%)
- 確定トレード: 94件 (TP 31 / SL 61 / EXP 2)
- 最新: AIOT/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$327.71** / 初期 $100.00 (+227.71%)
- 確定: 2814件 (Win 885 / Loss 923 / Flat 1006) / skip 2393件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ANSEM/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $327.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.19** / 初期 $100.00 (+5.19%)
- 確定: 647件 (Win 153 / Loss 159 / Flat 335) / skip 1410件
- 成長率目線: 平均log +0.000078 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0128 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $105.19

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.48** / 初期 $100.00 (-0.52%)
- 確定: 39件 (Win 14 / Loss 25 / Flat 0) / pending 0件 / skip 77件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000303 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $99.48

## 6. Latest Market Context

- 更新: 2026-07-13T17:36:12.352240+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=62142.0
- Funnel: target 867 → liquid 163 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.0 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIOT/USDT:USDT | +17.99% | $2,401,207.65 |
| EVAA/USDT:USDT | +13.26% | $19,963,619.97 |
| ALLO/USDT:USDT | +9.30% | $22,927,995.50 |
| VELVET/USDT:USDT | +4.69% | $28,985,453.01 |
| SKHYSTOCK/USDT:USDT | +2.60% | $3,218,226.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +3.74% | +3.92% |
| EVAA/USDT:USDT | below_1h_threshold | +2.38% | +2.57% |
| KITE/USDT:USDT | below_1h_threshold | +2.10% | +2.29% |
| EDGE/USDT:USDT | below_1h_threshold | +2.03% | +2.22% |
| SYN/USDT:USDT | below_1h_threshold | +1.40% | +1.58% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
