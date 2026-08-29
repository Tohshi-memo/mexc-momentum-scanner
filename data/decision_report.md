# Decision Report

- generated_at: 2026-08-29T13:01:18.051535+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12939**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12939, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.59% | **-1.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 8/20 | 40.0% | +3.42% | **+1.37%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.83% | **+0.73%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | -0.80% | **-0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.79% | **+2.79%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +3.33% | **+2.66%** |
| LIMIT_2PCT_LONG | 9/20 | 45.0% | +2.25% | **+1.01%** |
| LIMIT_8PCT_LONG | 3/20 | 15.0% | +5.33% | **+0.80%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +1.77% | **+0.71%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$731.83** / 初期 $100.00 (+631.83%)
- 確定: 4709件 (Win 1428 / Loss 1545 / Flat 1736) / skip 4791件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTR/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $731.83

## 4. Robust Adaptive DryRun ($100)

- 残高: **$160.81** / 初期 $100.00 (+60.81%)
- 確定: 2023件 (Win 555 / Loss 487 / Flat 981) / skip 4327件
- 成長率目線: 平均log +0.000235 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0766 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTR/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $160.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.26** / 初期 $100.00 (+15.26%)
- 確定: 2033件 (Win 596 / Loss 791 / Flat 646) / pending 4件 / skip 2373件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000180 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTR/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.26

## 6. Latest Market Context

- 更新: 2026-08-29T13:01:07.101970+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=77566.2
- Funnel: target 1023 → liquid 141 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TOAD/USDT:USDT | +87.69% | $1,984,094.68 |
| HNT/USDT:USDT | +71.67% | $10,235,944.92 |
| 4/USDT:USDT | +55.56% | $3,192,733.93 |
| BTR/USDT:USDT | +33.61% | $8,145,840.46 |
| LONGXIA/USDT:USDT | +21.93% | $1,910,727.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIVER/USDT:USDT | below_1h_threshold | +0.70% | +0.69% |
| DEXE/USDT:USDT | below_1h_threshold | +0.48% | +0.48% |
| 4/USDT:USDT | below_1h_threshold | +0.44% | +0.43% |
| TURBO/USDT:USDT | below_1h_threshold | +0.39% | +0.38% |
| BANK/USDT:USDT | below_1h_threshold | +0.23% | +0.22% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
