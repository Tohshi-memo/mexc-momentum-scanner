# Decision Report

- generated_at: 2026-07-07T15:16:04.361259+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8440**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8440, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.36% | **-1.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 10/20 | 50.0% | +1.30% | **+0.65%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.67% | **+0.50%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.35% | **+0.40%** |
| LIMIT_8PCT | 2/20 | 10.0% | -0.15% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +2.03% | **+2.03%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.40% | **+1.92%** |
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.96% | **+1.18%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.63% | **+0.98%** |

## 2. $100 Live Portfolio

- 残高: **$100.55** / 初期 $100.00 (+0.55%)
- 確定トレード: 69件 (TP 23 / SL 45 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.55
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$321.65** / 初期 $100.00 (+221.65%)
- 確定: 2647件 (Win 844 / Loss 896 / Flat 907) / skip 2354件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $321.65

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.48** / 初期 $100.00 (+5.48%)
- 確定: 640件 (Win 152 / Loss 158 / Flat 330) / skip 1211件
- 成長率目線: 平均log +0.000083 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0254 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TAC/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $105.48

## 5. Latest Market Context

- 更新: 2026-07-07T15:15:58.065771+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=63526.0
- Funnel: target 847 → liquid 172 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +93.02% | $16,933,152.84 |
| BLUR/USDT:USDT | +40.66% | $13,318,523.93 |
| EDGE/USDT:USDT | +25.09% | $6,874,348.49 |
| M/USDT:USDT | +20.63% | $1,031,038.34 |
| ALLO/USDT:USDT | +14.20% | $27,860,769.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EDGE/USDT:USDT | below_1h_threshold | +4.17% | +4.18% |
| CHIP/USDT:USDT | below_1h_threshold | +2.16% | +2.18% |
| APE/USDT:USDT | below_1h_threshold | +1.75% | +1.77% |
| UAI/USDT:USDT | below_1h_threshold | +1.61% | +1.62% |
| RAVE/USDT:USDT | below_1h_threshold | +1.24% | +1.26% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
