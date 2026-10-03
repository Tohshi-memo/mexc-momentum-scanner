# Decision Report

- generated_at: 2026-10-03T02:16:21.324406+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16030**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16030, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.95%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.95% | **-0.95%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 15/20 | 75.0% | +2.06% | **+1.55%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.72% | **+0.57%** |
| LIMIT_BB3S | 5/18 | 27.8% | +1.74% | **+0.48%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.22% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.16% | **+0.98%** |
| LIMIT_8PCT_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.01% | **+0.56%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +1.18% | **+0.47%** |
| MARKET_LONG | 20/20 | 100.0% | +0.45% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$120.27** / 初期 $100.00 (+20.27%)
- 確定トレード: 229件 (TP 82 / SL 140 / EXP 7)
- 最新: SI/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.27
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,320.19** / 初期 $100.00 (+1220.19%)
- 確定: 6135件 (Win 1810 / Loss 1966 / Flat 2359) / skip 6456件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $1,320.19

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.46** / 初期 $100.00 (+174.46%)
- 確定: 3606件 (Win 1005 / Loss 845 / Flat 1756) / skip 5835件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0451 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $274.46

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4191件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000181 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-03T02:16:12.869457+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=84585.0
- Funnel: target 1099 → liquid 174 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LONGXIA/USDT:USDT | +39.28% | $16,995,365.86 |
| VELVET/USDT:USDT | +16.57% | $8,617,100.33 |
| NIGHT/USDT:USDT | +9.33% | $10,626,807.87 |
| CT/USDT:USDT | +8.06% | $10,856,806.22 |
| SAND/USDT:USDT | +6.83% | $83,552,672.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LONGXIA/USDT:USDT | below_1h_threshold | +4.37% | +4.39% |
| CT/USDT:USDT | below_1h_threshold | +3.09% | +3.10% |
| SAND/USDT:USDT | below_1h_threshold | +1.56% | +1.58% |
| SYN/USDT:USDT | below_1h_threshold | +1.46% | +1.47% |
| ONE/USDT:USDT | below_1h_threshold | +1.23% | +1.25% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
