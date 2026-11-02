# Decision Report

- generated_at: 2026-11-02T15:36:26.633151+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18028**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18028, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.10% | **+0.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.36% | **+0.61%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.31% | **+0.22%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.13% | **+0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.62% | **+1.70%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.95% | **+1.33%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.64% | **+1.31%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.88% | **+1.15%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +2.21% | **+0.77%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 258件 (TP 95 / SL 155 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,566.44** / 初期 $100.00 (+1466.44%)
- 確定: 6880件 (Win 1997 / Loss 2206 / Flat 2677) / skip 7709件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LYN/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $1,566.44

## 4. Robust Adaptive DryRun ($100)

- 残高: **$385.32** / 初期 $100.00 (+285.32%)
- 確定: 4468件 (Win 1200 / Loss 993 / Flat 2275) / skip 6971件
- 成長率目線: 平均log +0.000302 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0517 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LYN/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $385.32

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6187件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000235 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-02T15:36:13.604935+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=77754.2
- Funnel: target 1093 → liquid 154 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARIA/USDT:USDT | +47.04% | $3,831,662.85 |
| LYN/USDT:USDT | +34.75% | $3,345,503.76 |
| HOT/USDT:USDT | +14.54% | $1,523,017.54 |
| EVAA/USDT:USDT | +11.84% | $5,636,932.10 |
| KORU/USDT:USDT | +9.70% | $81,990,317.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAMX/USDT:USDT | below_1h_threshold | +3.87% | +3.96% |
| EVAA/USDT:USDT | below_1h_threshold | +3.53% | +3.63% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +2.92% | +3.01% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +1.76% | +1.85% |
| AIN/USDT:USDT | below_1h_threshold | +1.08% | +1.17% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
