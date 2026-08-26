# Decision Report

- generated_at: 2026-08-26T08:11:22.015919+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12682**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12682, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +0.82% | **+0.16%** |
| LIMIT_7PCT | 5/20 | 25.0% | +0.08% | **+0.02%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.26% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.67% | **+1.42%** |
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.76% | **+1.32%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.83% | **+0.91%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.27% | **+0.76%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$687.36** / 初期 $100.00 (+587.36%)
- 確定: 4585件 (Win 1392 / Loss 1506 / Flat 1687) / skip 4658件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PONS/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $687.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.32** / 初期 $100.00 (+56.32%)
- 確定: 1979件 (Win 537 / Loss 473 / Flat 969) / skip 4114件
- 成長率目線: 平均log +0.000226 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0467 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BMT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $156.32

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.22** / 初期 $100.00 (+16.22%)
- 確定: 1959件 (Win 575 / Loss 747 / Flat 637) / pending 5件 / skip 2191件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000384 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BMT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $116.22

## 6. Latest Market Context

- 更新: 2026-08-26T08:11:11.304697+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=79055.7
- Funnel: target 1018 → liquid 166 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTR/USDT:USDT | +148.79% | $10,451,642.10 |
| BMT/USDT:USDT | +44.64% | $12,263,488.13 |
| LONGXIA/USDT:USDT | +31.58% | $1,920,783.43 |
| TAC/USDT:USDT | +27.34% | $5,043,763.61 |
| LIGHT/USDT:USDT | +18.74% | $1,074,677.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BMT/USDT:USDT | below_1h_threshold | +1.83% | +1.62% |
| JUP/USDT:USDT | below_1h_threshold | +1.30% | +1.09% |
| BTR/USDT:USDT | below_1h_threshold | +1.21% | +1.00% |
| COW/USDT:USDT | below_1h_threshold | +1.00% | +0.79% |
| USELESS/USDT:USDT | below_1h_threshold | +0.83% | +0.62% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
