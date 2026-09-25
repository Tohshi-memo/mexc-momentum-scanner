# Decision Report

- generated_at: 2026-09-25T17:31:27.767413+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15536**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15536, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.87%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.87% | **-1.87%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 15/20 | 75.0% | +1.08% | **+0.81%** |
| LIMIT_5PCT | 2/20 | 10.0% | +4.48% | **+0.45%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.07% | **+0.32%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.23% | **+0.18%** |
| LIMIT_ATR | 17/20 | 85.0% | -0.24% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.84% | **+1.29%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.55% | **+0.93%** |
| MARKET_LONG | 20/20 | 100.0% | +0.84% | **+0.84%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.62% | **+0.81%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.68% | **+0.67%** |

## 2. $100 Live Portfolio

- 残高: **$120.55** / 初期 $100.00 (+20.55%)
- 確定トレード: 222件 (TP 81 / SL 135 / EXP 6)
- 最新: APT/USDT:USDT EXPIRED PnL -0.12% 残高後 $120.55
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,207.62** / 初期 $100.00 (+1107.62%)
- 確定: 5903件 (Win 1741 / Loss 1891 / Flat 2271) / skip 6194件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NEAR/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.56% 残高後 $1,207.62

## 4. Robust Adaptive DryRun ($100)

- 残高: **$256.32** / 初期 $100.00 (+156.32%)
- 確定: 3469件 (Win 952 / Loss 793 / Flat 1724) / skip 5478件
- 成長率目線: 平均log +0.000271 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0248 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PHA/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $256.32

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.91** / 初期 $100.00 (+19.91%)
- 確定: 3171件 (Win 933 / Loss 1255 / Flat 983) / pending 0件 / skip 3838件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000181 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: XPL/USDT:USDT `MARKET` EXPIRED account -0.07% 残高後 $119.91

## 6. Latest Market Context

- 更新: 2026-09-25T17:31:16.609521+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=83626.6
- Funnel: target 1067 → liquid 171 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LYN/USDT:USDT | +43.46% | $3,066,251.25 |
| BR/USDT:USDT | +10.87% | $8,184,865.87 |
| GRASS/USDT:USDT | +9.52% | $1,507,252.52 |
| AERO/USDT:USDT | +5.91% | $2,319,058.06 |
| PHA/USDT:USDT | +5.16% | $12,354,855.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GRASS/USDT:USDT | below_1h_threshold | +4.95% | +5.06% |
| BR/USDT:USDT | below_1h_threshold | +4.31% | +4.42% |
| MVLL/USDT:USDT | below_1h_threshold | +2.07% | +2.18% |
| TAKE/USDT:USDT | below_1h_threshold | +1.89% | +2.00% |
| XPL/USDT:USDT | below_1h_threshold | +1.86% | +1.97% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
