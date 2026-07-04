# Decision Report

- generated_at: 2026-07-04T07:05:43.644317+00:00
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

- 更新: 2026-07-04T07:05:38.737665+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=62450.2
- Funnel: target 834 → liquid 153 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ANSEM/USDT:USDT | +75.26% | $4,792,068.05 |
| TLM/USDT:USDT | +58.38% | $42,359,461.64 |
| HMSTR/USDT:USDT | +49.77% | $4,429,902.63 |
| LAB/USDT:USDT | +41.94% | $48,133,412.00 |
| VELVET/USDT:USDT | +39.10% | $26,052,075.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MAGMA/USDT:USDT | below_1h_threshold | +1.95% | +1.99% |
| BEAT/USDT:USDT | below_1h_threshold | +1.40% | +1.43% |
| TAC/USDT:USDT | below_1h_threshold | +1.35% | +1.38% |
| HMSTR/USDT:USDT | below_1h_threshold | +1.25% | +1.29% |
| ANSEM/USDT:USDT | below_1h_threshold | +1.13% | +1.16% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
