# Decision Report

- generated_at: 2026-07-04T06:56:11.555254+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8229**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8229, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-2.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.50% | **-2.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 9/20 | 45.0% | +1.23% | **+0.55%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.44% | **+0.36%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.85% | **+0.18%** |
| LIMIT_8PCT | 3/20 | 15.0% | +1.14% | **+0.17%** |
| LIMIT_BB3S | 5/18 | 27.8% | +0.14% | **+0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.32% | **+2.32%** |
| ASK_LONG | 20/20 | 100.0% | +2.08% | **+2.08%** |
| LIMIT_2PCT_LONG | 9/20 | 45.0% | +3.08% | **+1.38%** |
| LIMIT_3PCT_LONG | 7/20 | 35.0% | +3.69% | **+1.29%** |
| LIMIT_1PCT_LONG | 12/20 | 60.0% | +2.15% | **+1.29%** |

## 2. $100 Live Portfolio

- 残高: **$102.10** / 初期 $100.00 (+2.10%)
- 確定トレード: 57件 (TP 20 / SL 36 / EXP 1)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$314.34** / 初期 $100.00 (+214.34%)
- 確定: 2546件 (Win 795 / Loss 847 / Flat 904) / skip 2244件
- 成長率目線: 平均log +0.000450 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $314.34

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.09** / 初期 $100.00 (+7.09%)
- 確定: 625件 (Win 150 / Loss 150 / Flat 325) / skip 1015件
- 成長率目線: 平均log +0.000110 / 幾何平均 +0.011% per trade / maxDD +3.57%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0861 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $107.09

## 5. Latest Market Context

- 更新: 2026-07-04T06:56:05.543548+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=62472.9
- Funnel: target 834 → liquid 154 → pre 50 → checked 50 → surge 5 → strict 3
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.8 >= 65=1, 4h RSI 93.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ANSEM/USDT:USDT | +74.29% | $4,789,645.09 |
| TLM/USDT:USDT | +61.65% | $43,754,766.09 |
| HMSTR/USDT:USDT | +50.79% | $4,286,888.17 |
| LAB/USDT:USDT | +42.45% | $48,656,469.00 |
| BAS/USDT:USDT | +31.82% | $4,235,893.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| S/USDT:USDT | below_1h_threshold | +3.57% | +3.53% |
| BSB/USDT:USDT | below_1h_threshold | +2.80% | +2.76% |
| MIRA/USDT:USDT | below_1h_threshold | +1.89% | +1.85% |
| POPCAT/USDT:USDT | below_1h_threshold | +1.73% | +1.69% |
| TAIKO/USDT:USDT | below_1h_threshold | +1.16% | +1.12% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
